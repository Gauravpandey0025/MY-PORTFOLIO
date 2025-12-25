const express = require('express');
const nodemailer = require('nodemailer');
const cors = require('cors');
require('dotenv').config();

const app = express();
const PORT = process.env.PORT || 3000;

app.use(cors());
app.use(express.json());

app.post('/send', async (req, res) => {
  const { name, email, message } = req.body || {};
  if (!name || !email || !message) return res.status(400).json({ error: 'Missing fields' });

  const user = process.env.GMAIL_USER;
  const pass = process.env.GMAIL_PASS;
  if (!user || !pass) return res.status(500).json({ error: 'Mail server not configured' });

  try {
    const transporter = nodemailer.createTransport({
      service: 'gmail',
      auth: {
        user,
        pass
      }
    });

    const mailOptions = {
      from: `${name} <${email}>`,
      to: 'rockaman1982@gmail.com',
      subject: `Portfolio message from ${name}`,
      text: `Name: ${name}\nEmail: ${email}\n\n${message}`
    };

    const info = await transporter.sendMail(mailOptions);
    return res.json({ ok: true, info });
  } catch (err) {
    console.error('Send error', err);
    return res.status(500).json({ error: 'Failed to send message', detail: err.toString() });
  }
});

app.listen(PORT, () => console.log(`Mail server running on port ${PORT}`));
