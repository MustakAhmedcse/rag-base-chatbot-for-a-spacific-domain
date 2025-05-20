# Banglalink Retailer App Guide

## 📱 What is the Banglalink Retailer App?
The Banglalink Retailer App is a mobile application designed for Banglalink retailers to sell recharge, varius offers, check commission, SIM cards stock, and manage retail operations efficiently.


## 🌐 Language Support
- **Available Languages:**
  - English
  - Bangla (বাংলা)
- Users can switch between languages from the **Profile** > **Settings** section.

### Welcome Screen

- **Logo and Title**: Displays the Banglalink logo and **“BL Retailer App”** text. Includes a language toggle (বাংলা / English).
- **Navigation Logic**:
  - **Logged-in users** with a valid session (within 3 days) are redirected to the **Dashboard**.
  - **New users** with no prior registration are taken to the **Device Registration** page.
  - **Expired sessions** (after 3 days of inactivity) redirect to the **Login** page.
- **Note**: Sessions expire after 3 days for security, requiring re-login.

### Device Registration

- Required for first-time use or new devices. Up to **5 devices** (1 Primary + 4 Secondary) can be registered.
- **Primary vs. Secondary Device**:
  - The **first registered device** is the **Primary Device**, with full control to manage other devices.
  - Additional devices are **Secondary Devices**, which can view the account but cannot manage settings unless promoted to primary.
- **Steps to Register**:
  1. On the **Device Registration** page, enter your **iTopUp number** in the *“Your iTopUp number”* field.
  2. Tap **Send** to receive a 6-digit OTP via SMS.
  3. Enter the **OTP** in the provided field. Use **Resend** if the OTP is not received.
  4. After successful OTP verification, proceed to the **Change Password** page.
  5. On **Change Password**:
     - Enter the **Temporary Password** (from the OTP message).
     - Set and confirm a **New Password**.
     - Tap **Save**.
  6. Redirected to the **Login** page to log in with the new password.
- **UI Elements**:
  - Title: **“Device Registration”**.
  - Input field: *Your iTopUp number*.
  - **Send** button.
  - Links: *Terms & Conditions*, *Privacy Policy*.
- **Device Limit**: If 5 devices are already registered, a message appears: **“Your device limit exceeded. Do you want to request for a new device?”**
  - **Cancel**: Dismisses the dialog.
  - **OK**: Sends a device extension request to Banglalink admin.
- **Troubleshooting**:
  - **Invalid Number**: Verify the iTopUp number (include country code if needed).
  - **OTP Not Received**: Ensure network connectivity and tap **Resend**.
  - **Registration Failure**: Check device limit or contact support.

### Login

- **Steps to Log In**:
  1. On the **Login** page, enter your **iTopUp Number** and **Password**.
  2. (Optional) Check **Remember Me** for a 3-day session.
  3. Tap **Login** to access the **Dashboard**.
- **Additional Links**:
  - *Forgot Password*: Initiates password reset via OTP.
  - *Terms & Conditions*, *Privacy Policy*: Open respective documents.
- **Troubleshooting**:
  - **Wrong Credentials**: Verify number and password.
  - **Forgot Password**: Use the link or contact support.
  - **Session Expiry**: Log in again after 3 days.

## Dashboard

The **Dashboard** is the main hub, offering quick access to features and key data.

- **Header Section**:

  - Displays **Retailer Name**.
  - **Search box** for customer numbers or account data.
  - **Notifications** icon with unread count.
  - Down-arrow to expand balances: *iTopUp Balance*, *SIM Balance*, *Scratch Card Balance*.

- **Quick Recharge Section**:

  - Fields: *“Mobile Number”*, *“Amount”*.
  - Enter details and tap **Pay** or arrow to initiate recharge.
  - **History** icon to view recent transactions.

- **Shortcut Icons**:

  - Icons for **Transaction**, **Commission**, **Campaign**, etc., linking to respective pages.

- **Sales Summary Section**:

  - Displays metrics like *SIM Sales*, *Scratch Card Sales*, *iTopUp Sales* for today.
  - Includes *Today’s Sales Memo*, *3 Days Memo History*, and a **Sales Trend Chart**.

- **Footer Navigation Bar**:

  - Icons: **Home**, **SIM Sales**, **iTopUp**, **Commission**, **Menu (☰)** (accesses Profile, Campaigns, Devices, etc.).

- **Using Dashboard Features**:

  - **Recharge**: Use Recharge section or **iTopUp** icon.
  - **Transaction History**: Tap **History** or **Transaction** icon.
  - **Commissions**: Tap **Commission** icon.
  - **Campaigns**: Tap **Campaign** icon.
  - **Search**: Find customer numbers or account data.

- **Troubleshooting**:

  - **Data Not Updating**: Check internet and swipe to refresh.
  - **Missing Recharges/Sales**: Verify date filters.

## Recharge (Top-Up)

The **Recharge** feature enables topping up customer mobile balances or selling offers.

- **Accessing Recharge**:

  - Tap **iTopUp** (footer or Quick Access) or use **Recharge** fields on Dashboard.
  - Tabs: **EV Recharge** (general recharges), **Amar Offer** (personalized offers).

- **Single EV Recharge**:

  1. On **EV Recharge** tab, enter **Customer Mobile Number** and **Recharge Amount**.
  2. Tap **Pay** when enabled.
  3. On **Confirmation** page, verify:
     - Customer Number
     - Recharge Amount
     - Commission
  4. Enter **EV PIN** and tap **Confirm**.
  5. **Success** message shows customer number and **New Balance**. Tap **OK**.

- **Multi EV Recharge**:

  1. Enter first customer’s number and amount, tap **Plus (+)** to add.
  2. Repeat for multiple customers.
  3. Tap **Pay** to view confirmation screen with all entries and total commission.
  4. Enter **EV PIN** and tap **Confirm**.
  5. **Success** message lists numbers and **New Balance**. Tap **OK**.

- **Amar Offer (Iris Offer) Recharge**:

  1. On **Amar Offer** tab, enter **Customer Mobile Number**.
  2. Tap **Show All Offer** to fetch personalized offers.
  3. (Optional) Filter by category (Voice, Data, Bundle, etc.).
  4. Select an offer (shows *Title*, *Duration*, *Cost Amount*, *Commission*).
  5. On confirmation page, verify details, enter **EV PIN**, and tap **Confirm**.
  6. **Success** screen shows number and new balance. Tap **OK**.

- **UI Elements**:

  - **History** icon for recent transactions.
  - **Send/Arrow** or **Pay** button.
  - Page title: **“Recharge”**.

- **Troubleshooting**:

  - **Recharge Failure**: Verify EV PIN, balance, and number format.
  - **Invalid Number**: Double-check number.
  - **Missing History**: Refresh or check date filter.

## Transactions (History)

- **Access**: Tap **History** icon on Recharge page or **Transaction** icon on Dashboard.
- **Tabs**:
  - **RECHARGE**: Lists customer recharge transactions (date, number, amount).
  - **INCOMING**: Lists commission and lifting records.
- **Steps**:
  1. Tap **History** to open **Transaction Page**.
  2. Switch between **Recharge** and **Incoming** tabs.
  3. Use date filters to narrow results.
- **UI Elements**:
  - Scrollable list with details (date, time, amount).
  - Page title: **“Transactions”**.
- **Troubleshooting**:
  - **Missing Transaction**: Check tab and date range.
  - **Empty List**: Ensure recharges or commissions exist.

## Commission

- **Access**: Tap **Commission** icon in footer.
- **Page Overview**:
  - **Sales vs Commission (Summary)**:
    - Shows **Total Commission** for the current month.
    - Breaks down by type (iTopUp, SIM, campaign bonuses).
    - Includes sales figures for context.
  - **Commission Details**:
    - Lists individual records (date, source, amount).
    - Filterable by date range.
  - **Retailer Statement**:
    - Downloadable PDF for the month, including retailer info, commission, and lifting data.
- **Steps**:
  1. Tap **Commission** to view **Sales vs Commission**.
  2. Check **Commission Details** for records.
  3. Download PDF via **Statement** button.
- **UI Elements**:
  - Page title: **“Commission”**.
  - Tabs: **Sales vs Commission**, **Commission Details**.
  - Lists with date, description, amount.
- **Troubleshooting**:
  - **Missing Commissions**: Check **Commission Details** or statement.
  - **Delayed Updates**: Wait until end of day or contact support.
  - **Incorrect Filters**: Verify date range.

## Campaigns

- **Access**: Menu (☰) → **Campaign**.
- **Campaign Page**:
  - Lists active campaigns as cards (title, duration, highlights).
  - Page title: **“Campaign”**.
- **Campaign Details**:
  - Tap a card to view objectives, targets, and rewards.
  - Tap **Enroll** to participate.
- **After Enrolling**:
  - Track progress (units sold vs. target) with bars or percentages.
  - Monitor bonus eligibility or rank.
- **UI Elements**:
  - Campaign list (grid/list).
  - **Enroll** button.
  - Progress indicators.
- **Troubleshooting**:
  - **Inactive Enroll Button**: Already enrolled.
  - **No Campaigns**: None active.
  - **Delayed Progress**: Wait for sales to update.

## Raise Complaint

- **Access**: Menu → **Raise Complaint**.
- **Raise Complaint Page**:
  - Fields:
    - **Complaint Type**: Select category (e.g., Service Issue, Billing).
    - **Complaint Title**: Brief title.
    - **Complaint Details**: Detailed description.
    - **Upload Image**: Optional photo/screenshot.
  - Tap **Submit** to send.
- **Complaint History**:
  - Tap **History** icon to view past complaints (status: Pending, Resolved).
  - **View** button for details and responses.
- **Steps**:
  1. Open **Raise Complaint**.
  2. Fill fields, attach image if needed, and tap **Submit**.
  3. Check **Complaint History** for status.
- **UI Elements**:
  - Page title: **“Raise Complaint”**.
  - Input fields, upload button, **Submit** button, **History** icon.
- **Troubleshooting**:
  - **Submission Failure**: Check internet and required fields.
  - **Missing Complaint**: Verify account and date filters.
  - **Clarity**: Keep complaints concise with screenshots if helpful.

## Communications (Updates & Training)

- **Access**: Menu → **Communications**.
- **Tabs**:
  - **Communications**: Announcements and updates.
  - **Training Materials**: Guides, videos, or documents.
  - **Archived**: Older content with search functionality.
- **Steps**:
  1. Browse **Communications** for updates.
  2. Check **Training Materials** for resources.
  3. Use **Archived** to find past content.
- **UI Elements**:
  - Tabs: *Communications, Training Materials, Archived*.
  - Lists with title, date.
- **Troubleshooting**:
  - **Content Not Loading**: Check internet.
  - **Outdated Content**: Refresh or use search/filters.

## Best Practices

- **Access**: Menu → **Best Practices**.
- **Best Practices List**: Community-driven tips with descriptions and optional images.
- **Contributing**:
  1. Tap **+ (Add)** button.
  2. On **Add Best Practice**, enter description and optional image.
  3. Tap **Submit** to add to list.
- **UI Elements**:
  - Page title: **“Best Practices”**.
  - **Add (+)** button.
  - List of entries.
- **Troubleshooting**:
  - **Submission Failure**: Ensure image is JPEG/PNG and not too large.
  - **Clarity**: Keep descriptions concise, use existing entries as examples.

## Device List (Device Management)

- **Access**: Menu → **Device List**.
- **UI Elements**:
  - Page title: **“Device List”**.
  - List of devices (name, registration date), with **Primary Device** indicated.
  - Toggle switches and buttons for management.
- **Device Management (Primary Device Only)**:
  - **Enable/Disable**: Toggle to control device access.
  - **Make Primary**: Promote a secondary device, demoting the current primary.
  - **Deregister**: Remove a device.
  - **Disable All**: Block all devices.
  - **Deregister All**: Remove all devices.
- **Steps**:
  1. Review device list.
  2. Use **Deregister**, **Make Primary**, or toggle to manage.
  3. Use **Disable All** or **Deregister All** for bulk actions.
- **Troubleshooting**:
  - **Lost Primary Device**: Re-register or contact support.
  - **Limit Reached**: Request extension (see Device Registration).
  - **Bulk Actions**: Use cautiously, as re-registration may be needed.

## Digital Services Installation

- **Access**: Menu → **Digital Service**.
- **Digital Service Installation Page**:
  - Fields:
    - **Product Type**: Dropdown (e.g., bKash, Nagad).
    - **MSISDN**: Customer mobile number.
  - Tap **Submit**, confirm prompt (*“Are you sure?”*).
- **Digital Service History**:
  - Lists past installations (Date, Product Name, MSISDN).
- **Steps**:
  1. Select **Product Type** and enter **MSISDN**.
  2. Tap **Submit** and confirm.
  3. Verify success message.
- **UI Elements**:
  - Page title: **“Digital Service Installation”**.
  - Input fields, **Submit** button, confirmation dialog, **History** page.
- **Troubleshooting**:
  - **Installation Failure**: Check number and network.
  - **Service Already Active**: Verify customer status.
  - **History Verification**: Check **Digital Service History**.

## Profile & Settings

- **Edit Profile**:
  - Access: Menu → **My Profile** or **Edit Profile**.
  - Edit Name, Email, Address, Profile Photo, then tap **Save**.
- **Change Password**:
  - Access: Menu (Profile/Settings).
  - Enter **Current Password**, **New Password** (twice), tap **Save**.
- **Logout**:
  - Access: Menu → **About** or Settings, tap **Logout**.
- **UI Elements**:
  - Editable fields, **Save** button, password fields, **Logout** option.
- **Troubleshooting**:
  - **Save Failure**: Validate fields (e.g., email format).
  - **Forgot Password**: Use **Forgot Password** flow.
  - **Post-Logout**: Log in again to resume.

## About & Support

- **About Section** (Menu → **About**):
  - **Review & Rating**: Opens Google Play Store.
  - **FAQ**: Common questions and answers.
  - **Terms & Conditions**, **Privacy Policy**: Official documents.
  - **Check for Update**: Prompts for app updates.
  - **Logout**: Signs out.
- **Help & Support**:
  - Provides contact info (phone/email) or refers to **FAQ**.
- **UI Elements**:
  - List of menu items.
- **Troubleshooting**:
  - **App Issues**: Check for updates or consult **FAQ**.
  - **Account Problems**: Contact Banglalink support.

## Troubleshooting Tips (Common Issues)

- **App Crashes/Freezes**: Update app, restart device, check internet.
- **No Internet**: Ensure data/Wi-Fi connection.
- **OTP Not Received**: Verify network, use **Resend OTP**, check number.
- **Invalid Credentials**: Confirm registered iTopUp number and password.
- **Session Expired**: Log in again after 3 days.
- **Recharge Failed**: Verify EV PIN, balance, number. Retry or check balance.
- **Commission/Balance Issues**: Refresh page, contact support with records.
- **Device Limit**: Request extension for 6th device.
- **Outdated Content**: Refresh lists or check for updates.