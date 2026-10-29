# DANIIL SLEPOV

<img src="https://github.com/MoldyDanya.png" width="150" align="right" style="border-radius: 50%; margin-left: 20px;">

**Email:** dev@dslepov.ru | **Telegram:** @MoldyDanya | **Phone:** +7 (905) 775-02-90  
**Location:** Moscow, Kurskaya metro station | **Work Format:** Remote (not available for relocation or business trips)

---

## PROFILE

Game developer with 6+ years of experience in Unity development, Game Design, DevOps automation, and QA management. Broad skill set: from game systems development and Unity project migration to building CI/CD infrastructure and team management.

**Real-world CI/CD automation examples** (GitHub Actions workflows, Fastlane deployment configs) in my portfolio: https://github.com/MoldyDanya/devops-portfolio

**Key Achievements:**
- Led the development of a planar graph puzzle game prototype: created GDD and mechanics design, developed visual editor and balance tools, implemented UI (UI Toolkit), designed FTUE, coordinated the team (Unity dev, UI artist, VFX dev)

*Unity Development:*
- Performed Unity project migrations to new versions (major and minor): updated APIs, fixed breaking changes, improved components, updated and fixed packages/assets/SDKs to working state (projects: Offroad Outlaws, No Limits Drag Racing 2 from Unity 2022.3.40 to Unity 6000.1.11; Steel Rage to new Unity version)
- Developed vehicle systems: two-wheeled vehicle stabilization, full-featured headlight system, configured visually realistic physics (dynamic suspensions, wheel and body deformation, snowmobile ski behavior via raycast and Jobs)
- Developed automation tools: localization (DeepL API + Unity Localization for 3 projects), automatic component relinking via reflection

*Game Design:*
- Designed level design for Grand Wars PvP map: reworked the map for a new genre, increased size by 2.5x, created themed zones with props, placed loot, configured capturable territories, balanced timings for PvP fairness
- Worked with game assets: selected weapons, characters, skins, pets, drones, localized names and descriptions, configured sounds and VFX
- Balanced game content: all weapon parameters (damage, fire rate, accuracy, recoil, blast radius), character stats (health, speed, armor, abilities), economic systems (prices, rewards, upgrades)
- Developed an automatic weapon balance generation tool in Google Sheets with Google Apps Script: system took input parameters and automatically calculated all characteristics

*DevOps and CI/CD:*
- Reduced Unity project build time from 1+ hour to 30-40 minutes, deployment from 2+ hours to 50-60 minutes
- Achieved 99%+ uptime for AWS infrastructure, reduced failed builds by 80%
- Designed and administered AWS infrastructure: 4 EC2 servers (2 CPU for builds, 1 GPU for UI tests, 1 dev), on-demand provisioning with automatic start/stop, AMI snapshots for quick recovery
- Fully automated deployment via Fastlane: Android → Google Play (Internal/Beta/Production), iOS → TestFlight

*QA and Testing:*
- Created QA department from scratch, scaled from 1 to 3 specialists with clear processes and roles
- Supported three studio projects from start to release
- Developed comprehensive performance testing system: automatic metrics collection (FPS, loading, memory), sending to Google Sheets via C# API, automated benchmarks with camera routes
- Created QA automation tools: two Telegram bots (state cleanup via Selenium + reference database for promo codes), cross-platform Kivy application for game state editing, Bash/OBS scripts for interval screen recording

*Management and Leadership:*
- Led QA department of 3 people: distributed tasks, monitored execution, mentored newcomers
- Conducted interviews and was responsible for hiring QA candidates
- Mentored second game designer: assigned tasks, reviewed execution, provided feedback

**Specialization:** Unity (C#, DOTS, ECS, UI Toolkit, Photon), DevOps (AWS, GitHub Actions, Docker, Fastlane), Game Design (mechanics, balance, level design, FTUE, economy), QA automation (performance/security testing), team management, technical leadership.

---

## KEY COMPETENCIES

**DevOps and Cloud Technologies**
AWS EC2, AMI snapshots, on-demand provisioning, monitoring (Grafana, AWS CloudWatch), alerting (Slack), incident management, Docker, Docker Compose

**CI/CD Automation**
GitHub Actions (multi-trigger workflows: manual/scheduled/automated), modular and reusable workflows, custom build caching, semantic versioning via git tags, Fastlane (deployment to Google Play and TestFlight)

**Unity Development (C# Development)**
C#, UI Toolkit, DOTS, Playmaker, Zenject, ECS, OOP, SOLID, game systems prototyping, tools development

**Game Design and Content Balance**
Game Design Documents, mechanics and level design, weapon and character balance, economic systems, content integration, localization

**Testing and QA**
AltTester (CI/CD integration for UI testing), automated and manual testing, performance testing, security testing, cracked build analysis, QA process organization, QA team management

**Tools and Processes**
Git, Plastic SCM, Jira, Trello, Notion, ClickUp, Figma, Agile methodologies, team management, technical leadership

**Programming Languages**
C#, Python, Bash, Ruby, JavaScript, Google Script

---

## WORK EXPERIENCE

### Ajika Games | DevOps Engineer & Unity Developer (Unity Mobile Projects)
**November 2024 - September 2025 (11 months)**
Location: China (remote work) | Work Format: outstaffing for Battle Creek Games projects
**Projects:** [Offroad Outlaws](https://play.google.com/store/apps/details?id=com.battlecreek.offroadoutlaws), [No Limit Drag Racing 2](https://play.google.com/store/apps/details?id=com.battlecreek.nolimit2)

**Cloud Infrastructure (AWS)**
- Designed and maintained AWS infrastructure for Unity mobile projects (Android/iOS), selected optimal EC2 instance types considering requirements for computing power, memory, and storage
- Administered 4 EC2 servers in production:
  - 2 CPU-optimized servers for project builds
  - 1 GPU-optimized server for automated UI testing
  - 1 development server
- Ensured high infrastructure availability (uptime >99%)
- Implemented on-demand provisioning system: EC2 instances automatically started before builds and stopped on idle timer to optimize costs
- Created and maintained AMI snapshots for server changes to enable quick recovery in case of incidents
- Configured comprehensive monitoring via Grafana and AWS CloudWatch with Prometheus integration for metrics collection
- Implemented automatic Slack alerts for proactive issue detection

**CI/CD Automation (GitHub Actions)**
- Developed and maintained modular GitHub Actions workflows for Unity projects with encapsulation: project changes and CI/CD logic changes didn't affect each other
- Implemented flexible multi-trigger build system:
  - Manual builds (on-demand builds)
  - Scheduled nightly builds (automatic nightly builds)
  - Auto-test triggers (automatic test execution under certain conditions)
- Fully automated deployment pipeline via Fastlane:
  - Android → Google Play (with track selection: Internal/Beta/Production)
  - iOS → TestFlight via Xcode on macOS GitHub-hosted runners
- Created intuitive workflow interface with clear parameters for one-click builds and deployment
- Developed custom caching system to accelerate builds under GitHub Actions minutes limitation
- Implemented semantic versioning system via git tags with automatic version increments

**Unity Development**
- Upgraded two projects (Offroad Outlaws, No Limits Drag Racing 2) from Unity 2022.3.40 to Unity 6000.1.11 (major version): updated APIs, fixed breaking changes, improved components
- Integrated and updated SDKs (Facebook, AppLovin, Firebase) for both projects, ensured compatibility with new Unity versions

**Incident Management and Error Analysis**
- Conducted deep root cause analysis of failed builds and server incidents
- Documented issues, their causes, and solutions to prevent recurrence
- Integrated AltTester framework into CI/CD pipeline for automated UI testing:
  - Configured execution on GPU server with virtual display support (Xvfb, Openbox)
  - Installed and configured OpenGL and NVIDIA Driver
- Ensured uninterrupted CI/CD operation during Unity project upgrade to new major version
- Reduced failed builds by 80% through proactive analysis and recurring error prevention

**Key Results**
- Reduced build time from 1+ hour to 30-40 minutes
- Reduced deployment time from 2+ hours to 50-60 minutes
- Fully automated delivery pipeline from commit to TestFlight/Google Play
- Achieved 99%+ infrastructure uptime
- Reduced recurring incidents through preventive documentation and automated checks

---

### Ajika Games | Unity Developer & Game Designer
**November 2022 - November 2024 (2 years 1 month)**
Location: China (remote work)
**Projects:** Studio internal development prototypes, [Offroad Outlaws](https://play.google.com/store/apps/details?id=com.battlecreek.offroadoutlaws), [No Limit Drag Racing 2](https://play.google.com/store/apps/details?id=com.battlecreek.nolimit2), [Offroad Outlaws Drag Racing](https://play.google.com/store/apps/details?id=com.battlecreek.nolimit2dirtdrags), [American Marksman](https://play.google.com/store/apps/details?id=com.battlecreek.americanmarksman)

**Planar Graph Puzzle Prototype (Unity DOTS)**
- Led development of innovative puzzle game prototype (untangling planar graphs) with no direct market analogues, coordinated team (Unity developer, UI artist, VFX developer)
- Created complete Game Design Document describing core gameplay mechanics, designed game mechanics
- Developed visual editor for designing and configuring planar graphs
- Created tools for flexible and quick adjustment of level difficulty balance
- Implemented user interface via UI Toolkit with transition animations and interactivity
- Developed tutorial and First Time User Experience (FTUE)

**Runner Prototype (Unity DOTS)**
- Developed enemy AI using Unity DOTS

**Top-Down Shooter Prototype**
- Developed enemy spawn system and AI logic (state machine)

**Ajika Vehicle System Prototype**
- Integrated and configured visualization of physically accurate dynamic vehicle suspension
- Developed headlight system (on/off, low/high beam, turn signals, brake lights, reverse lights)
- Configured driver animations (steering wheel rotation, looking back during reverse, inertial swaying with vehicle physics)
- Configured visualization of physically accurate wheel deformation
- Implemented vehicle switching system (tap to change vehicle)
- Configured realistic vehicle body deformation via parameter system: part durability, element dependencies, deformation weights
- Developed route-following mechanics (waypoints):
  - Created compass system (arrow above car pointing to nearest waypoint)
  - Configured about 10 different routes across the map (placed route starts, checkpoints, and finishes)
  - Implemented best result saving
- Performed migration from custom vehicle physics to NWH Vehicle Physics asset near end of prototype development

**Project Localization (Offroad Outlaws, No Limits Drag Racing 2, American Marksman)**
- Developed automated localization system in Google Sheets with DeepL API integration and Unity Localization
- Organized localization process for three projects:
  - Team added placeholders to localization table
  - Replaced placeholders with correct text
  - Automatically generated translations via developed system
  - Reviewed and improved translation quality in subsequent iterations
  - Synchronized translations in Unity project with table

**Offroad Outlaws Drag Racing**
- Developed surface type detection system under vehicle wheels
- Created custom tools for automatic transform bone relinking via reflection: in legacy project each vehicle bone had separate reference, making new vehicle addition extremely labor-intensive
- Implemented two-wheeled vehicle stabilization system
- Enhanced Photon network synchronization code: extended legacy logic that only supported straight-line movement by adding correct synchronization on uneven maps with elevation changes
- Built and tested game builds
- Analyzed and enhanced game mechanics for Freeride mode
- Tested map for Freeride mode
- Developed in-game currency earning methods and game activities for Freeride mode
- Developed physically accurate visualization of snowmobile ski behavior

**Unity Analytics - Analytics Event Audit and Refactoring**
- Developed automated Selenium parser to export all analytics events and parameters from Unity Analytics to Google Sheets (Unity Analytics had no built-in export)
- Conducted comprehensive analytics event audit per Battle Creek Games request:
  - Analyzed which events were registered and used in projects
  - Identified unused events for removal
  - Determined necessary events for addition
  - Developed unified naming convention for all analytics events (there was none)
  - Renamed all events to unified naming standard
  - Throughout work period, added new events and periodically analyzed errors for fixes

**Comprehensive Product Analysis (Offroad Outlaws, No Limits Drag Racing 2, American Marksman)**
- Conducted complete analysis of three products per Battle Creek Games request
- Compiled detailed document with identified issues and improvement suggestions:
  - UX (user experience) problems
  - Discovered bugs
  - Inconveniences and shortcomings in game mechanics
  - Specific recommendations for fixes and improvements

**Web Development and Presentation**
- Developed first version of ajika.games website: implemented layout and supervised further improvements
- Developed team presentation structure and prepared texts

---

### GD Company (ForgeGames Mobile) | Lead Game Designer & Unity Developer
**June 2021 - October 2022 (1 year 5 months)**
Project: [Grand Wars](https://play.google.com/store/apps/details?id=com.gdcompany.grandwars.mafiacity)

**Game Design and Documentation**
- Developed complete set of Game Design Documents for all game features with technical specifications
- Designed game map considering PvP balance and player experience
- Developed automatic weapon balance generation tool in Google Sheets with Google Apps Script integration: on button press, system took input parameters, performed complete characteristic calculations, and automatically added ready item to game config, eliminating need for manual editing
- Developed tutorial and First Time User Experience (FTUE)

**Balance and Content Management (Game Designer)**
- Balanced all weapon parameters in game (damage, fire rate, accuracy, recoil, blast radius)
- Configured character stats (health, speed, armor, special abilities)
- Balanced economic systems (prices, rewards, upgrade costs)
- Interpreted analytics data for iterative player experience optimization
- Selected all game assets (weapons, characters, skins, pets, drones, gang members)
- Developed and localized names and descriptions for all game items
- Configured sounds and visual effects

**Game System Implementation (Unity Developer)**
- Implemented game logic for battle event system (Armored Car, Bank Robbery)
- Developed dynamic character skin system with real-time switching support
- Configured character animations with weapons (stances, shooting, reloading)
- Fixed critical bugs affecting gameplay

**Level Design (Game Designer)**
- Reworked old map for new genre and increased size by 2.5x with new game zones
- Divided map into diverse themed game zones
- Filled zones with props and decorations
- Calculated timings and balanced routes/map elements for PvP fairness
- Evenly distributed loot across map
- Configured capturable territory mechanics

**Battle Pass (Game Designer)**
- Filled battle pass seasons with rewards
- Balanced progression (points per task, completion time)

**Buff/Debuff Systems (Game Designer)**
- Created positive and negative effect system with documentation
- Balanced duration, intensity, and effect interactions

**Leadership (Lead Game Designer)**
- Supervised second game designer's work: assigned tasks, reviewed execution, provided feedback, conducted mentoring
- Conducted smoke and integration testing of game systems before QA handoff
- Assigned testing tasks to QA team with detailed functionality descriptions

**Technical Work (Unity Developer)**
- Performed Steel Rage project migration to new Unity version with component improvements, API updates, and breaking change fixes
- Integrated updated SDKs (Facebook, AppLovin, Firebase)
- Worked on content integration and technical implementation in Unity

---

### GD Company (ForgeGames Mobile) | QA Engineer Lead
**February 2019 - June 2021 (2 years 5 months)**
Projects: [Pacific Warships](https://play.google.com/store/apps/details?id=com.gdcompany.deepwaters&hl=en), [Steel Rage](https://play.google.com/store/apps/details?id=com.gdcompany.robocars.shooterwarfare), [War After](https://play.google.com/store/apps/details?id=com.gdcompany.modernshooter.warfareops), [Grand Wars](https://play.google.com/store/apps/details?id=com.gdcompany.grandwars.mafiacity)

**QA Process Organization (QA Engineer Lead)**
- Created QA department from scratch: scaled from one specialist to team of 3 people with clear processes and roles
- Conducted interviews, was responsible for hiring and selecting QA candidates
- Supported three studio projects from start to release
- Distributed tasks among employees, monitored execution, and mentored newcomers

**Test Documentation**
- Developed complete set of test documentation: test suites, test cases, checklists for regression and functional testing
- Reviewed Game Design Documents and mockups for potential issues before development launch
- Maintained ongoing test documentation updates as projects evolved

**Testing (Android/iOS)**
- Conducted unit, integration, functional, regression, and ad-hoc testing
- Applied white-box and black-box methods to validate application logic and behavior
- Analyzed text reviews and videos from various platforms to identify production issues
- Captured logs from mobile devices via ADB for error and crash diagnostics

**Automation and Tool Development**
- Developed comprehensive performance testing system with automatic metrics collection (FPS, loading, memory) and sending to Google Sheets via custom C# API integration for subsequent analysis
- Created automated benchmark system: algorithm for launching game sessions with special camera moving along specified routes, with automatic performance statistics collection and aggregation in editor and on devices
- Implemented secure dev tools access system via Google Sheets: user authorization, dynamic launch parameter loading, automatic new request registration via Google Apps Script
- Implemented debug UI with dev-tool controls: mode switching, metrics visualization, quick access to frequently used functions
- Developed two Telegram bots: (1) game state cleanup automation via Selenium integration with backend admin panel, (2) reference bot with promo code and dev-command database for all studio projects
- Created cross-platform Kivy (Python) application for editing local game state files on PC and Android to simplify functionality testing
- Automated testing process via Bash/OBS scripts: interval recording of two screens with automatic time marking for quick bug analysis and reproduction

**Security Testing**
- Conducted security testing: searched for application hacking methods and analyzed cracked builds to identify vulnerabilities

---

## EDUCATION AND LANGUAGES

**Education**  
A.N. Kosygin Russian State University  
Bachelor of Applied Mathematics and Computer Science (2013 - 2017)

**Languages**  
- **Russian** - native  
- **English** - B1 (Intermediate): working with technical documentation, communication with international teams

**Certificates**  
- [Learn C# Course - Sololearn, 2022](https://www.sololearn.com/Certificate/CT-ZUZBDWNF/png)
- [C# Course - Codecademy, 2022](https://www.codecademy.com/profiles/daniilSlepov1798965862/certificates/65f0ff88f4fc58e0536b3b51648dff24)

