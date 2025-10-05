import streamlit as st
import torch
import torch.nn as nn
from torchvision import models, transforms as T
from PIL import Image
import os
from datetime import datetime

# Page config
st.set_page_config(
    page_title="Fresh2Feed 🍎", 
    layout="wide", 
    initial_sidebar_state="expanded"
)

# Custom CSS for beautiful UI
st.markdown("""
<style>
    .main-header {
        text-align: center;
        padding: 2rem 0;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border-radius: 10px;
        margin-bottom: 2rem;
    }
    .metric-card {
        background: white;
        padding: 1.5rem;
        border-radius: 10px;
        box-shadow: 0 2px 8px rgba(0,0,0,0.1);
        text-align: center;
    }
    .donation-card {
        background: white;
        padding: 1.5rem;
        border-radius: 10px;
        box-shadow: 0 2px 8px rgba(0,0,0,0.1);
        margin-bottom: 1rem;
    }
    .stButton>button {
        width: 100%;
        border-radius: 8px;
        padding: 0.5rem 1rem;
        font-weight: 600;
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state
if 'current_view' not in st.session_state:
    st.session_state.current_view = "Donor"
if 'donations' not in st.session_state:
    st.session_state.donations = []
if 'donor_points' not in st.session_state:
    st.session_state.donor_points = {}
if 'donor_name' not in st.session_state:
    st.session_state.donor_name = ""
if 'donor_location' not in st.session_state:
    st.session_state.donor_location = "Mumbai"

# Pre-registered NGO
NGO_NAME = "Mumbai Food Bank"
NGO_LOCATION = "Mumbai"

# AI Model Setup
@st.cache_resource
def load_model():
    """Load the pre-trained food freshness detection model"""
    class_names = ['rottenoranges', 'rottenbananas', 'rottenapples', 'apples', 'oranges', 'banana']
    num_classes = len(class_names)
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    
    # Load model architecture
    model = models.resnet18(pretrained=True)
    in_features = model.fc.in_features
    model.fc = nn.Linear(in_features, num_classes)
    
    # Try to load saved weights
    model_path = 'best_train.pt'
    model_url = 'https://github.com/tumblr-byte/Fresh2Feed/releases/download/v1.0.0/best_train.pt'
    
    try:
        # Check if model exists locally
        if not os.path.exists(model_path):
            st.sidebar.info("📥 Downloading AI model from GitHub...")
            import urllib.request
            urllib.request.urlretrieve(model_url, model_path)
            st.sidebar.success("✅ Model downloaded successfully!")
        
        model.load_state_dict(torch.load(model_path, map_location=device))
    except Exception as e:
        st.sidebar.warning(f"⚠️ Using demo model (Error: {str(e)})")
    
    model.to(device)
    model.eval()
    
    return model, class_names, device

# Image transforms
test_transforms = T.Compose([
    T.Resize((224, 224)),
    T.ToTensor()
])

def predict_freshness(image, model, class_names, device):
    """Predict if food is fresh or rotten"""
    img_tensor = test_transforms(image).unsqueeze(0).to(device)
    
    with torch.no_grad():
        output = model(img_tensor)
        pred_idx = torch.argmax(output, dim=1)
        label = class_names[pred_idx.item()]
    
    # Check if rotten
    is_rotten = 'rotten' in label.lower()
    return label, is_rotten

def get_badge(points):
    """Return badge based on points"""
    if points >= 100:
        return "🏆 Gold Hero"
    elif points >= 50:
        return "🥈 Silver Champion"
    elif points >= 20:
        return "🥉 Bronze Contributor"
    else:
        return "⭐ Food Saver"

# ============ DONOR VIEW ============
def donor_view():
    # Header
    st.markdown("""
    <div class="main-header">
        <h1>🍎 Fresh2Feed - Fighting Hunger Together</h1>
        <p>Donor Portal: Share your leftover food with those in need</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Donor info input
    col1, col2 = st.columns(2)
    with col1:
        donor_name = st.text_input("Your Name:", value=st.session_state.donor_name, placeholder="Enter your name")
        if donor_name:
            st.session_state.donor_name = donor_name
    
    with col2:
        donor_location = st.selectbox(
            "Your Location:", 
            ["Mumbai", "Delhi", "Bangalore", "Chennai", "Kolkata", "Hyderabad"],
            index=["Mumbai", "Delhi", "Bangalore", "Chennai", "Kolkata", "Hyderabad"].index(st.session_state.donor_location)
        )
        st.session_state.donor_location = donor_location
    
    if not st.session_state.donor_name:
        st.info("👆 Please enter your name to start donating")
        return
    
    # Show donor stats
    points = st.session_state.donor_points.get(st.session_state.donor_name, 0)
    badge = get_badge(points)
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown(f"""
        <div class="metric-card">
            <h3 style="color: #667eea;">{points}</h3>
            <p>Your Points</p>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown(f"""
        <div class="metric-card">
            <h3>{badge}</h3>
            <p>Your Badge</p>
        </div>
        """, unsafe_allow_html=True)
    with col3:
        st.markdown(f"""
        <div class="metric-card">
            <h3>📍 {donor_location}</h3>
            <p>Location</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Donation form
    st.subheader("🍽️ Donate Food")
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        uploaded_file = st.file_uploader("Upload food image", type=['jpg', 'jpeg', 'png'], help="Upload a clear image of the food you want to donate")
        
        if uploaded_file:
            image = Image.open(uploaded_file).convert("RGB")
            st.image(image, caption="Your food donation", use_container_width=True)
    
    with col2:
        if uploaded_file:
            num_people = st.number_input("Number of people this can feed:", min_value=1, max_value=100, value=5, help="Estimate how many people can eat this food")
            
            st.markdown("<br>", unsafe_allow_html=True)
            
            if st.button("🚀 Submit Donation", type="primary", use_container_width=True):
                with st.spinner("🤖 AI is checking food freshness..."):
                    try:
                        model, class_names, device = load_model()
                        label, is_rotten = predict_freshness(image, model, class_names, device)
                        
                        if is_rotten:
                            st.error("❌ Sorry! Our AI detected rotten food. We cannot accept this donation for safety reasons.")
                            st.info(f"🔍 Detection Result: {label}")
                        else:
                            st.success("✅ Food looks fresh! Sending to NGOs...")
                            
                            # Add to donations
                            donation = {
                                'id': len(st.session_state.donations) + 1,
                                'donor': st.session_state.donor_name,
                                'location': st.session_state.donor_location,
                                'image': image,
                                'people_fed': num_people,
                                'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M"),
                                'status': 'Pending',
                                'ai_label': label
                            }
                            st.session_state.donations.append(donation)
                            
                            st.balloons()
                            st.success(f"🎉 Donation submitted successfully!")
                            st.info(f"📤 Notification sent to: **{NGO_NAME}** in {NGO_LOCATION}")
                            st.info(f"🔍 AI Detection: Fresh {label.replace('rotten', '').title()}")
                            
                    except Exception as e:
                        st.error(f"Error processing image: {str(e)}")
    
    # Show donation history
    st.markdown("---")
    st.subheader("📜 Your Donation History")
    
    user_donations = [d for d in st.session_state.donations if d['donor'] == st.session_state.donor_name]
    
    if user_donations:
        for donation in reversed(user_donations):
            status_color = "green" if donation['status'] == 'Approved' else "orange"
            status_icon = "✅" if donation['status'] == 'Approved' else "⏳"
            
            with st.expander(f"{status_icon} Donation #{donation['id']} - {donation['timestamp']} - {donation['status']}"):
                col1, col2 = st.columns([1, 2])
                with col1:
                    st.image(donation['image'], use_container_width=True)
                with col2:
                    st.write(f"**People Fed:** {donation['people_fed']} 👥")
                    st.write(f"**Location:** {donation['location']} 📍")
                    st.write(f"**Status:** :{status_color}[{donation['status']}]")
                    if donation['status'] == 'Approved':
                        st.success(f"Points earned: +{donation['people_fed'] * 2}")
    else:
        st.info("📭 No donations yet. Start donating to earn points and badges!")

# ============ NGO VIEW ============
def ngo_view():
    # Header
    st.markdown(f"""
    <div class="main-header">
        <h1>🏢 Fresh2Feed - Fighting Hunger Together</h1>
        <p>NGO Dashboard: {NGO_NAME} ({NGO_LOCATION})</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Calculate stats
    location_donations = [d for d in st.session_state.donations if d['location'] == NGO_LOCATION]
    approved_donations = [d for d in location_donations if d['status'] == 'Approved']
    total_donations = len(approved_donations)
    total_meals = sum([d['people_fed'] for d in approved_donations])
    pending_count = len([d for d in location_donations if d['status'] == 'Pending'])
    
    # Display stats
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown(f"""
        <div class="metric-card">
            <h2 style="color: #667eea;">{total_donations}</h2>
            <p>Total Donations Approved</p>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown(f"""
        <div class="metric-card">
            <h2 style="color: #28a745;">{total_meals}</h2>
            <p>Total Meals Fed</p>
        </div>
        """, unsafe_allow_html=True)
    with col3:
        st.markdown(f"""
        <div class="metric-card">
            <h2 style="color: #ff6b6b;">{pending_count}</h2>
            <p>Pending Approvals</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Pending donations
    st.subheader("📥 Incoming Donations (Pending Approval)")
    
    pending_donations = [d for d in location_donations if d['status'] == 'Pending']
    
    if pending_donations:
        for donation in pending_donations:
            st.markdown(f"""
            <div class="donation-card">
                <h3>🎁 Donation #{donation['id']}</h3>
            </div>
            """, unsafe_allow_html=True)
            
            col1, col2, col3 = st.columns([1, 2, 1])
            
            with col1:
                st.image(donation['image'], use_container_width=True)
            
            with col2:
                st.write(f"**👤 Donor:** {donation['donor']}")
                st.write(f"**📍 Location:** {donation['location']}")
                st.write(f"**👥 Can feed:** {donation['people_fed']} people")
                st.write(f"**🕐 Time:** {donation['timestamp']}")
                st.write(f"**🤖 AI Check:** ✅ Fresh {donation['ai_label'].replace('rotten', '').title()}")
            
            with col3:
                st.markdown("<br>", unsafe_allow_html=True)
                if st.button(f"✅ Approve Donation", key=f"approve_{donation['id']}", type="primary", use_container_width=True):
                    # Update donation status
                    for d in st.session_state.donations:
                        if d['id'] == donation['id']:
                            d['status'] = 'Approved'
                    
                    # Award points to donor
                    donor_name = donation['donor']
                    if donor_name not in st.session_state.donor_points:
                        st.session_state.donor_points[donor_name] = 0
                    points_earned = donation['people_fed'] * 2
                    st.session_state.donor_points[donor_name] += points_earned
                    
                    st.success(f"✅ Donation approved! {donor_name} earned {points_earned} points!")
                    st.rerun()
            
            st.markdown("---")
    else:
        st.info("📭 No pending donations at the moment. Check back later!")
    
    # Approved donations
    st.markdown("<br>", unsafe_allow_html=True)
    st.subheader("✅ Approved Donations History")
    
    if approved_donations:
        for donation in reversed(approved_donations):
            with st.expander(f"✅ Donation #{donation['id']} - {donation['timestamp']}"):
                col1, col2 = st.columns([1, 2])
                with col1:
                    st.image(donation['image'], use_container_width=True)
                with col2:
                    st.write(f"**👤 Donor:** {donation['donor']}")
                    st.write(f"**👥 People Fed:** {donation['people_fed']}")
                    st.write(f"**📍 Location:** {donation['location']}")
                    st.write(f"**🕐 Time:** {donation['timestamp']}")
                    st.success("Status: Approved & Delivered")
    else:
        st.info("📭 No approved donations yet. Start approving donations to track your impact!")

# ============ MAIN APP ============
def main():
    # Sidebar
    with st.sidebar:
        st.title("🍎 Fresh2Feed")
        st.markdown("### Fighting Hunger Together")
        
        st.markdown("---")
        
        # View selector
        st.subheader("👁️ Switch View")
        view = st.radio(
            "Select View:",
            ["Donor", "NGO"],
            index=0 if st.session_state.current_view == "Donor" else 1,
            help="Toggle between Donor and NGO views to see both sides of the platform"
        )
        st.session_state.current_view = view
        
        st.markdown("---")
        
        # Info section
        if view == "Donor":
            st.info("🎁 **Donor View**\n\nDonate food and earn points!")
        else:
            st.success(f"🏢 **NGO View**\n\n{NGO_NAME}\n📍 {NGO_LOCATION}")
        
        st.markdown("---")
        st.markdown("### 🎯 App Features")
        st.markdown("✅ AI-powered freshness detection")
        st.markdown("✅ Real-time donation tracking")
        st.markdown("✅ Gamification & badges")
        st.markdown("✅ Location-based matching")
        
        st.markdown("---")
        st.markdown("### 📊 Global Impact")
        total_global_meals = sum([d['people_fed'] for d in st.session_state.donations if d['status'] == 'Approved'])
        st.metric("Total Meals Fed", total_global_meals)
        
        st.markdown("---")
        st.caption("Built for social good 💚")
    
    # Route to correct view
    if st.session_state.current_view == "Donor":
        donor_view()
    else:
        ngo_view()

if __name__ == "__main__":
    main()
