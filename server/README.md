Gmail SMTP mail server for portfolio

1. Copy `.env.example` to `.env` and fill values:

```
GMAIL_USER=your.email@gmail.com
GMAIL_PASS=your_app_password_here
PORT=3000
```

2. Create an App Password in your Google Account (if you have 2FA enabled):
   - Sign in to Google Account → Security → App passwords → generate an app password for "Mail" and copy it.
   - Use that app password as `GMAIL_PASS` (do NOT use your account password).

3. Install and run server:

```bash
cd server
npm install
npm run start
```

4. Keep the server running on a machine reachable by your site. If you serve `index.html` from the same host (or proxy to this server), the form will POST to `/send` and the server will send the email via Gmail.

Security note: For production, prefer OAuth2 or a trusted transactional email provider. Do not commit `.env` with secrets.
