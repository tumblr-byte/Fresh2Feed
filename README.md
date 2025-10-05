# 🍎 Fresh2Feed - Fighting Hunger Together

**“Turning surplus food into meals for the hungry — fast, safe, and transparent.”**

## Project Overview
Fresh2Feed is an innovative platform designed to combat hunger by connecting food donors with NGOs. Our mission is to reduce food waste and ensure no one goes to bed hungry by creating a seamless bridge between surplus food and those in need.

---

## The Problem
- Millions of people go hungry every day.  
- Tons of edible **surplus food** from weddings, restaurants, family functions, and households are wasted.  
- No efficient system exists to connect food donors with NGOs serving those in need.  

---

## Our Solution
Fresh2Feed provides a simple, **working prototype** that demonstrates the core functionality of the platform.

### Current Prototype Workflow
1. **User Registration:** The judge (or demo user) registers by entering their **name** and **location**.  
2. **Donation Process (acting as Donor):**
   - Upload an image of the food (**currently only apples**).  
     - Image should be **good quality, close-up, and clear** for accurate AI evaluation.  
   - Choose the **number of people** the food can feed.  
   - Click **Process**.  
     - If the food is **fresh**, it moves to the NGO approval stage ✅  
     - If the food is **rotten**, it is rejected ❌  
3. **NGO Approval (acting as NGO):**
   - In the same session, the judge can **switch to NGO view** to see pending donations.  
   - For each request, they see:  
     - Uploaded apple image  
     - Number of people the food can feed  
     - Timestamp of submission  
     - Donor location  
   - Approve the request → points and badges are awarded to the donor.  

> **Note:** Since this is a **demo prototype**, both donor and NGO actions are performed by the same user. Data is **session-based**, so it resets when the browser is refreshed or closed.

---

### AI-Powered Quality Check
- Our **ResNet18 model** trained on fresh vs rotten apple images evaluates the uploaded food.  
- Ensures only **safe, quality food** is sent to NGOs.  

---

### Gamification & Motivation
To make donating fun and meaningful:

- **Point System:** Donors earn **2 points per person fed** when NGOs approve their donation.  
  - Example: Donate food for 10 people → Earn 20 points  

- **Badge Levels:**  
  - 🏆 **Gold Hero** - 100+ points  
  - 🥈 **Silver Champion** - 50-99 points  
  - 🥉 **Bronze Contributor** - 20-49 points  
  - ⭐ **Food Saver** - 0-19 points  

**Why Points Matter:**  
- Points provide **visual progress** and a sense of achievement.  
- Badges reflect contribution level and create **friendly competition**.  
- Social recognition encourages continued participation.  
- Dashboard shows **“You fed X people this session!”**, linking points to **real impact**.  

> **Current Limitation:** Pickup coordination is not yet implemented; this will be included in future versions.

---

## Demo Details
- **Food Type:** Apples (fresh vs rotten)  
- **Locations:** Simulated for multiple cities  
- **NGO:** Pre-registered demo NGO to approve donations  

---

## Technology Stack
- **Frontend:** Streamlit (Python web framework)  
- **AI Model:** PyTorch ResNet18 (trained on apple freshness dataset)  
- **Architecture:** Session-based prototype (data not persistent across browser refresh)  

---

## Future Scope
- Expand to **all food categories**: vegetables, cooked meals, packaged goods.  

- Implement **secure user registration** with **government ID verification** and **encrypted, tamper-proof profiles**, ensuring donor authenticity and preventing misuse.  

- Enable NGOs to **approve donations and coordinate pickup locations efficiently**.  

- Integrate **real-time GPS tracking** for donation pickups and delivery logistics.  

- Store user, donation, and NGO information in a **secure, decentralized/blockchain-inspired database** to prevent tampering or unauthorized access.  

- Develop a **mobile app** for easier access, notifications, and on-the-go donations.  

- Provide **multi-language support** to reach a wider, diverse audience.  

- Add **analytics dashboards** for NGOs to track food donations, meals served, and wastage reduction.  

- Implement **impact transparency**, showing donors exactly how their contribution helped, with real-time feedback and visual reports.


---

## Social Impact
Fresh2Feed addresses UN Sustainable Development Goals:
- **Goal 2:** Zero Hunger  
- **Goal 12:** Responsible Consumption and Production  

By reducing food waste and feeding the hungry, Fresh2Feed creates a **win-win solution** for society.

---




