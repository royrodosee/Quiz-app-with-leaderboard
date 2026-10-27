# ⚡ Quiz App with Leaderboard — Live Quiz & Leaderboard Web App

Quiz App with Leaderboard is a responsive, feature-rich web application offering a timed trivia experience with a live competitive leaderboard, transparent scoring formulas, immediate feedback, and guest/member account management.

---

## ✨ Key Features

### 🎮 Dynamic Quiz Experience
- **6 Rich Categories**:
  - 🔬 **Science & Nature** (Physics, Biology, Astronomy, Chemistry)
  - 💻 **Tech & Coding** (JavaScript, Python, Web Dev, Algorithms)
  - 🌍 **Geography & World** (Capitals, Landmarks, Rivers, Wonders)
  - 🏛️ **History & Empires** (Ancient Civilizations, Milestones, Leaders)
  - 🎬 **Pop Culture & Media** (Cinema, Video Games, Music, Heroes)
  - 🧠 **General Knowledge** (Puzzles, Curiosities, Trivia)
  - ✨ **All Categories Mix**
- **3 Balanced Difficulties**:
  - 🟢 **Easy**: 15s limit per question • 100 base pts
  - 🟡 **Medium**: 12s limit per question • 200 base pts
  - 🔴 **Hard**: 8s limit per question • 300 base pts
- **Custom Round Lengths**: 5, 10, or 15 questions per session.
- **Randomized Order**: Both questions and option choices are dynamically shuffled (Fisher-Yates) every time.

### ⏱️ Immediate Feedback & Live Timers
- Real-time animated countdown bar with visual urgency transitions (Green → Amber → Pulsing Red when under 3.5 seconds).
- **Instant Answer Validation**:
  - Correct answer lights up in emerald with checkmark.
  - Incorrect answer highlights in rose with shake animation and reveals the correct option.
  - Informative explanation box unfolds with trivia context for every question.
  - Live streak combo counter (`🔥 3x Streak (+50 pts)`).
- **Full Keyboard Navigation**:
  - Keys `1`, `2`, `3`, `4` or `A`, `B`, `C`, `D` to pick answers.
  - `Space` or `Enter` to advance to the next question.
  - `Esc` to close any modal.

### 📐 Transparent Scoring Formula
All points earned in Quiz App with Leaderboard are transparently calculated using three components:
```
Total Points = Base Points + Time Bonus + Streak Bonus
```
1. **Base Points**: Easy = 100 pts, Medium = 200 pts, Hard = 300 pts.
2. **Time Bonus**: Proportional to the remaining time on the clock:
   `Time Bonus = (RemainingSeconds / TotalLimitSeconds) * MaxBonus`
3. **Streak Bonus**: Active on 2+ consecutive correct answers:
   `Streak Bonus = (CurrentStreak - 1) * StreakMultiplier`
   *(Easy: +25/lvl, Medium: +50/lvl, Hard: +75/lvl)*

### 🏆 Live Global Leaderboard
- **Timeframe Filters**:
  - 📅 **Daily (Today)**: Scores submitted in the last 24 hours.
  - 🗓️ **Weekly (This Week)**: Scores submitted within the last 7 days.
  - 🌐 **All-Time**: All-time hall of fame.
- **Category & Difficulty Filters**: Filter the board by specific subjects or skill levels.
- **Top 3 Podium**: Elevated podium cards for 1st (Gold 👑), 2nd (Silver 🥈), and 3rd (Bronze 🥉).
- **User Highlighting**:
  - Current player's entry is highlighted with a glowing border and `YOU` badge.
  - Fixed / sticky bottom bar displaying `Your Placement: #X` with quick "Beat Score" replay.
- **Duplicate Prevention**: Unique session IDs prevent duplicate score submissions.

### 👤 Profile & Authentication
- **Play as Guest**: Jump in immediately with an auto-generated identity (e.g., `GuestExplorer#412`).
- **Custom Avatars & Names**: Choose from 12 avatars (🦊, 🦉, 🚀, 🤖, 🧙‍♂️, 🥷, 🦁, 🐉, etc.) and customize your display alias.
- **Member Registration & Login**: Upgrade to a registered member with password protection to safeguard high scores.
- **Lifetime Stats**: Track games played, high score, overall accuracy, and total points.

### 🎨 Design, Accessibility & Audio
- **Audio Synthesizer (Zero Dependencies)**: Built-in Web Audio API generator produces chimes, buzzer thuds, streak fanfares, clock ticks, and victory arpeggios. Persistent mute toggle included.
- **Theme Switcher**: Dark (sleek glowing console) and Light (clean high-contrast) modes.
- **Confetti Celebration**: Particle explosion on high-scoring performances.
- **Responsive Layout**: Designed for mobile touchscreens, tablets, and desktop displays.
- **Empty States**: Encouraging empty states when filters have no scores yet.

---

## 🚀 How to Run the App

### Option A: One-Click Windows Launch
Double-click `start.bat` in this folder:
```cmd
start.bat
```
This runs the Python server on `http://localhost:8000` and automatically opens your default web browser.

### Option B: Using Python
Run from the project root:
```bash
py server.py
# or
python server.py
```
Then visit `http://localhost:8000` in any web browser.

### Option C: Direct Browser Opening (No Server Required)
Open `index.html` directly in Google Chrome, Microsoft Edge, Firefox, or Safari. The app includes a complete client-side storage engine using `localStorage`, so everything works offline.

---

## 📁 File Structure
```
quiz-app/
├── index.html                 # Semantic single-page application structure
├── css/
│   └── styles.css             # Typography, animations, themes, and responsive design
├── js/
│   ├── data/
│   │   └── questions.js       # Curated 75+ question bank with categories & explanations
│   ├── sound.js               # Web Audio API procedural sound engine
│   ├── storage.js             # User profiles, auth, score persistence & deduplication
│   ├── quizEngine.js          # Gameplay loop, timers, scoring calculations & shuffling
│   ├── leaderboard.js         # Ranking algorithms, top podium & filters
│   └── app.js                 # State machine, keybindings, modals & toast alerts
├── data/
│   └── leaderboard.json       # Persisted server leaderboard storage (auto-created)
├── server.py                  # Lightweight HTTP & REST API server
├── start.bat                  # One-click Windows starter
└── README.md                  # Complete documentation
```
