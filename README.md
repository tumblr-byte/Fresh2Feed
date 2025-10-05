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
Fresh2Feed provides a two-sided platform:

### For Donors
Anyone can donate **surplus food** from weddings, restaurants, family functions, or home. The process is simple:
1. Enter your name and location.
2. Upload an image of the food (currently demonstrating with apples).
3. Specify how many people the food can feed.

### AI-Powered Quality Check
- Our trained **ResNet18 deep learning model** instantly analyzes the food image to determine freshness.  
- **Fresh food** → Approved and sent to local NGOs ✅  
- **Rotten/spoiled food** → Rejected for safety reasons ❌  
- Ensures only safe, quality food reaches those in need.

### For NGOs
- Receive real-time notifications of food donations in their area.  
- Review donation details (donor info, quantity, AI freshness verification).  
- Approve and coordinate pickup efficiently.  

### Gamification & Motivation
To encourage regular participation and make donating fun and meaningful, Fresh2Feed uses a points and badge system:

- **Point System:** Donors earn **2 points per person fed** when NGOs approve their donation.  
  - Example: Donate food for 10 people → Earn 20 points  

- **Badge Levels:**  
  - 🏆 **Gold Hero** - 100+ points (community champion)  
  - 🥈 **Silver Champion** - 50-99 points (dedicated contributor)  
  - 🥉 **Bronze Contributor** - 20-49 points (active helper)  
  - ⭐ **Food Saver** - 0-19 points (getting started)  

**Why Points Matter:**  
- Points provide **visual progress** and a sense of achievement.  
- Badges reflect the donor's contribution level and create **friendly competition**.  
- Social recognition encourages users to continue donating and share their impact with others.  
- Impact dashboard shows **“You fed X people this month!”**, linking points to **real-world outcomes**.  

> **Note:** For the current demo, NGOs only approve donations. Pickup coordination and logistics will be integrated in future versions.

---

## Current Demo
- **Food Type:** Fresh vs rotten apples (expandable to all food types)  
- **Locations:** 6 major Indian cities (Mumbai, Delhi, Bangalore, Chennai, Kolkata, Hyderabad)  
- **NGO:** Pre-registered "Mumbai Food Bank" serving all locations  

---

## Technology Stack
- **Frontend:** Streamlit (Python web framework)  
- **AI Model:** PyTorch ResNet18 (trained on food freshness dataset)  
- **Architecture:** Real-time session-based management  

---

## Future Scope
- Expand to **all food categories**: vegetables, cooked meals, packaged goods.  
- Allow **any user to register** with personal info and verify using **government ID** for security.  
- NGOs can **approve donations and coordinate pickup locations** based on availability and freshness.  
- Integrate **real-time GPS tracking** for donation pickups.  
- Add **database support** (PostgreSQL/MySQL) for storing users, donations, and NGO info.  
- Build a **mobile app** for easier access and notifications.  
- Provide **multi-language support** for wider reach.  
- Add **analytics dashboard** for NGOs to track donations, wastage reduction, and meals served.  
- Implement **impact transparency** → each donor can see how their donation reached those in need.  

---

## Social Impact
Fresh2Feed directly addresses UN Sustainable Development Goals:
- **Goal 2:** Zero Hunger  
- **Goal 12:** Responsible Consumption and Production  

By reducing food waste and feeding the hungry, Fresh2Feed creates a **win-win solution** for society.

---

