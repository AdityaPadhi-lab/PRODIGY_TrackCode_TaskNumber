const express = require("express");
const bcrypt = require("bcryptjs");
const jwt = require("jsonwebtoken");
const User = require("../models/User");
const { JWT_SECRET } = require("../config");

const router = express.Router();

// Register Route
router.post("/register", async (req, res) => {
    const { username, password } = req.body;

    const userExists = await User.findOne({ username });
    if (userExists) return res.status(400).json({ message: "User already exists" });

    const hashedPassword = await bcrypt.hash(password, 10);
    const user = new User({ username, password: hashedPassword });

    await user.save();
    res.json({ message: "User registered successfully" });
});

// Login Route
router.post("/login", async (req, res) => {
    const { username, password } = req.body;

    const user = await User.findOne({ username });
    if (!user) return res.status(400).json({ message: "User not found" });

    const isMatch = await bcrypt.compare(password, user.password);
    if (!isMatch) return res.status(400).json({ message: "Invalid password" });

    const token = jwt.sign({ userId: user._id }, JWT_SECRET, { expiresIn: "1h" });
    res.json({ token });
});

// Protected Route Example
router.get("/dashboard", async (req, res) => {
    const token = req.headers["authorization"];
    if (!token) return res.status(401).json({ message: "Access Denied" });

    try {
        const verified = jwt.verify(token, JWT_SECRET);
        res.json({ message: "Welcome to the dashboard", userId: verified.userId });
    } catch (err) {
        res.status(400).json({ message: "Invalid token" });
    }
});

module.exports = router;
