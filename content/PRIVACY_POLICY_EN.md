# PoolPilot — Privacy Policy

This policy describes PoolPilot version 1 and this website. **Effective date: 16 October 2026. Last updated: 27 October 2026.**

## Contact

PoolPilot is published by **Arnaud Mourcel, a French sole proprietor (entrepreneur individuel, EI) and micro-entrepreneur**, 244 rue de Bègles, 33800 Bordeaux, France. Contact: **arnaudmourcel47@gmail.com**; telephone: **06 45 48 02 03**. Professionals using PoolPilot enter information about their own customers and must manage it in line with their applicable obligations. The publisher has no remote access to records stored only in the app; the professional remains responsible for using their own customers' contact details.

## Information used

The app lets users record customer contact details and addresses, notes, pool and equipment information, appointments, service visits, water measurements, products used, maintenance work, photos, and a business profile with a logo. Users enter or select this information. PoolPilot does not require an in-app user account.

The app also uses its settings, local reminder information, and the subscription status needed to show access rights. In the flows reviewed, PoolPilot receives only the images the user selects through Apple's Photos picker; it does not request broad photo library access.

## Storage and purposes

Professional records stay in the app's local storage on the device, using SwiftData and files in Application Support. Imported images are resized and stored as files; data models keep only relative file paths. This information is used to display and edit records, plan routes, schedule reminders, and generate PDF reports.

Version 1 does not use CloudKit to synchronize records. The code audit found no publisher-operated server, advertising SDK, or analytics SDK integrated into the commercial target. Device backups managed by iOS may include app data depending on the user's settings; they are separate from PoolPilot CloudKit synchronization.

## Apple services and user-initiated actions

- **Photos:** users choose the images to import. PoolPilot's working copies are stored locally.
- **Local notifications:** with permission, PoolPilot schedules maintenance reminders on the device. Reminder text may include a pool name or task and may appear on the lock screen according to iOS settings.
- **Maps, phone, and email:** opening directions passes the chosen address to Apple Maps; call and email actions open the corresponding apps with the selected details. Those services are governed by their own settings and policies.
- **Subscriptions:** Apple supplies and verifies products, purchases, and entitlements through StoreKit. PoolPilot does not receive payment card numbers. An unverified transaction does not grant Pro access.
- **Sharing:** a PDF or backup leaves the app only when the user chooses a destination through the iOS share sheet or Files. That destination, which may be iCloud Drive, is subject to its own policy.

## Backups, security, and retention

Manual `.poolpilotbackup` archives contain professional records and photos. **PoolPilot does not encrypt these archives.** Users should keep them in a secure location and control who receives them. PoolPilot checks archive integrity before offering restoration. A restore may retain an earlier local generation to allow rollback. Exported PDFs and archives are prepared in temporary folders and subject to app cleanup; copies saved or shared elsewhere remain under the control of their destination or recipient.

Data stays on the device until the user edits or deletes it, chooses a restore, or removes the app and its data through iOS. Some operations retain professional history: deleting a customer does not necessarily delete associated pools and service visits. External copies and system backups must be managed separately.

## Choices and requests

Users can view their records and export a backup even after a Pro subscription expires. They can edit or delete items where the app provides that action. The publisher has no remote access to records stored only on the device; contacting the publisher alone therefore cannot delete a local copy or a backup shared elsewhere. For questions about data or applicable rights, write to **arnaudmourcel47@gmail.com**.

Where applicable, individuals may request access to, rectification or erasure of their personal data, or restriction of processing, and may object to processing or request portability when those rights apply. For customer records held only by a professional on their device, contact that professional first: the publisher cannot inspect or change those records remotely. A complaint may be lodged with the **CNIL** through [cnil.fr](https://www.cnil.fr/fr/plaintes).

## Visiting the public website

The PoolPilot information website is hosted on **GitHub Pages**. Its source contains no contact form, analytics, advertising script, or asset fetched from a third-party network. Visiting a page nevertheless connects the browser to GitHub's servers, which may process technical connection data under its [privacy statement](https://docs.github.com/en/site-policy/privacy-policies/github-general-privacy-statement). The publisher does not use that data to track website visitors. External links open other services at the visitor's request.

If a visitor writes to **arnaudmourcel47@gmail.com**, their email address, message content and any attachments are used to respond and, where needed, to follow up on support. Handling support requests is based on the publisher's legitimate interest in providing support; requests to exercise privacy rights are handled to comply with applicable legal obligations. Correspondence is available to the publisher and passes through **Gmail (Google)**. Under [Google's documentation](https://policies.google.com/privacy/frameworks?hl=en), data may be processed outside the European Economic Area. The publisher plans to delete support messages **no later than 12 months after the last exchange**, unless a legal duty or a documented dispute requires longer retention. The site has no contact form.

This policy will be updated if features, integrations, or processing practices change. It is available at **https://arnaudmourcel47-spec.github.io/poolpilot-site/en/privacy/**.
