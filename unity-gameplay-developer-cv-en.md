# DANIIL SLEPOV

<img src="https://github.com/MoldyDanya.png" width="150" align="right" style="border-radius: 50%; margin-left: 20px;">

**Unity Developer (C#, Game Systems, DOTS)**

**Email:** dev@dslepov.ru | **Telegram:** @MoldyDanya | **Phone:** +7 (905) 775-02-90  
**Location:** Moscow, Russia | **Work Format:** Remote (not open to relocation or business trips)

---

## ABOUT ME

Unity Developer with 6+ years of experience in game systems development, prototyping, and technical implementation of mechanics for mobile and PC projects.

Specialized in developing complex game systems: vehicle physics (dynamic suspension, stabilization, deformation via raycast and Jobs System), AI (DOTS, state machine), UI (UI Toolkit with animations), network code (Photon), internal development tools, and routine process automation.

Performed migration of two Unity projects from version 2022.3.40 to Unity 6000.1.11 (major update): updated APIs, fixed breaking changes, integrated updated SDKs (Facebook, AppLovin, Firebase), refined all components to working state.

Led development of innovative puzzle game prototype (untangling planar graphs): created GDD, developed visual editor for graph creation, balancing tools, built UI with UI Toolkit, coordinated team (Unity dev, UI artist, VFX dev).

Understand Game Design specifics from the inside (4 years of Game Designer experience): designed mechanics, balanced content, created GDDs, worked with level design and FTUE. Additional experience in DevOps (AWS, CI/CD) and QA (performance testing, automation) - useful for workflow optimization and code quality.

**Example of Match-3 core gameplay implementation** (Unity) - in my portfolio: https://github.com/MoldyDanya/unity-match-3
**Comprehensive resume with full work experience** (Unity Development, Game Design, DevOps, QA, team management): [master-cv-en.md](https://github.com/MoldyDanya/my-cv/blob/main/master-cv-en.md)

---

## KEY SKILLS

**Unity and C# Development**  
C#, Unity Editor, Unity DOTS/ECS, UI Toolkit, Photon (multiplayer), Jobs System, Physics (raycast, collision detection), animations (Animator, Timeline), Reflection, OOP, SOLID, game systems prototyping, Editor tools development

**Game Systems and Mechanics**  
Vehicle physics (dynamic suspension, deformation, stabilization), AI systems (DOTS, state machine, pathfinding), network code (Photon synchronization), vehicle systems, localization (Unity Localization + DeepL API), Unity Analytics integration

**Migration and Integration**  
Unity project upgrades (major and minor versions, breaking changes, API updates), SDK integration and updating (Facebook, AppLovin, Firebase), legacy code maintenance, architecture refactoring

**Game Design**  
Game Design Documents, mechanics design, level design, content balancing (weapons, characters, economy), FTUE (First Time User Experience), gameplay prototyping

**Additional Skills**  
Performance optimization, profiling (Profiler, Frame Debugger), Git workflows, DevOps (CI/CD, AWS), QA automation (performance testing, C# API for metrics)

**Tools and Processes**  
Git, Plastic SCM, Jira, Trello, Notion, Visual Studio, Rider, Agile methodologies, code review, technical documentation

---

## WORK EXPERIENCE

### Ajika Games | DevOps Engineer & Unity Developer (Unity Mobile Projects)
**November 2024 - September 2025 (11 months)**  
Location: China (remote) | Format: Outstaffing for Battle Creek Games projects  
**Projects:** [Offroad Outlaws](https://play.google.com/store/apps/details?id=com.battlecreek.offroadoutlaws), [No Limit Drag Racing 2](https://play.google.com/store/apps/details?id=com.battlecreek.nolimit2)

DevOps Engineer and Unity Developer on two multiplayer mobile projects (Android/iOS). Full DevOps cycle: AWS infrastructure design, CI/CD pipeline management, automated testing integration. Unity development: project migration to new major version, SDK integration and updating.

**Unity Development (Project Migration):**

✔ Led complete upgrade of two projects from Unity 2022.3.40 to Unity 6000.1.11 (major update): updated APIs, fixed all breaking changes, refined components to working state

✔ Integrated and updated SDKs (Facebook, AppLovin, Firebase) for compatibility with new Unity version: rewrote deprecated integrations, ensured stable operation across all platforms

✔ Ensured uninterrupted CI/CD pipeline operation during migration: configured builds for new version, conducted testing on all platforms - avoided release cycle disruption

**Cloud Infrastructure (AWS):**

✔ Designed and maintained AWS infrastructure for Unity mobile projects: selected optimal EC2 instance types considering computational power, memory, and storage requirements

✔ Administered 4 EC2 servers in production (2 CPU for builds, 1 GPU for UI tests, 1 dev), ensured >99% uptime

✔ Implemented on-demand provisioning system: EC2 instances automatically started before build and stopped on idle timer to optimize costs

✔ Created and maintained AMI snapshots when making server changes for quick recovery in case of incidents

✔ Set up comprehensive monitoring via Grafana and AWS CloudWatch with Prometheus integration for metrics collection

✔ Implemented automated Slack alerts system for proactive problem detection

**CI/CD Automation (GitHub Actions):**

✔ Developed and maintained modular GitHub Actions workflows for Unity projects with encapsulation: project changes and CI/CD logic changes didn't affect each other

✔ Implemented flexible multi-trigger build system: Manual builds, Scheduled nightly builds, Auto-test triggers

✔ Fully automated deployment pipeline via Fastlane: Android → Google Play (Internal/Beta/Production), iOS → TestFlight via Xcode on macOS GitHub-hosted runners

✔ Created intuitive workflow interface with clear parameters for one-click builds and deployment

✔ Developed custom caching system to speed up Unity builds within GitHub Actions minutes limitation

✔ Implemented semantic versioning system via git tags with automatic version increments

**Incident Management:**

✔ Conducted deep root cause analysis of failed builds and server incidents, documented solutions to prevent recurrence

✔ Integrated AltTester framework into CI/CD pipeline for automated UI testing: configured execution on GPU server with virtual display support (Xvfb, Openbox), installed and configured OpenGL and NVIDIA Driver

✔ Reduced failed builds by 80% through proactive analysis and prevention of recurring errors

**Key Results:**

✔ Reduced build time from 1+ hour to 30-40 minutes, deployment from 2+ hours to 50-60 minutes

✔ Fully automated delivery pipeline from commit to TestFlight/Google Play

✔ Ensured infrastructure uptime of 99%+

✔ Successful migration of two production projects to Unity 6000.1.11 without development disruption

---

### Ajika Games | Unity Developer & Game Designer
**November 2022 - November 2024 (2 years 1 month)**  
Location: China (remote)  
**Projects:** Prototypes + multiplayer mobile projects (Offroad Outlaws, No Limits Drag Racing 2, Offroad Outlaws Drag Racing, American Marksman)

Unity game systems development and prototyping, Editor tools development, automation integration, Unity Analytics implementation, network code (Photon), localization. Additionally: Game Design (GDD, level design, content balancing).

**Prototyping and Project Leadership:**

✔ Led development of innovative puzzle game prototype (untangling planar graphs) with no direct market analogs, coordinated team (Unity dev, UI artist, VFX dev)

✔ Created complete Game Design Document describing core gameplay mechanics, designed game mechanics and difficulty progression

✔ Developed visual Editor tool for planar graph design and configuration: drag-and-drop interface, graph validation, export to runtime format

✔ Created tools for flexible and rapid difficulty level balancing

✔ Built user interface with UI Toolkit: transition animations, interactive elements, responsive layout

✔ Developed tutorial and FTUE (First Time User Experience): step-by-step mechanics training, hints, smooth difficulty introduction

**Game Systems Development:**

✔ Developed comprehensive vehicle physics system for Vehicle System project:
  • Integrated and configured physically accurate dynamic vehicle suspension visualization
  • Implemented two-wheeled vehicle stabilization (motorcycles, bicycles) through physics and balancing
  • Developed headlight system with full functionality (on/off, low/high beam, turn signals, brake lights, reverse lights)
  • Configured visually realistic wheel and vehicle body deformation through parameter system
  • Developed physically accurate ski behavior display system for snowmobile via raycast and Jobs System
  • Performed migration from custom physics to NWH Vehicle Physics asset near end of development

✔ Configured driver animations: steering wheel rotation (IK), looking back during reverse, inertial swaying with vehicle physics

✔ Developed vehicle switching system (tap to switch) with previous vehicle state preservation

✔ Developed route-based driving mechanics (waypoints):
  • Compass system (UI indicator pointing to nearest waypoint)
  • Configured ~10 different routes across map with checkpoints
  • Implemented best time saving and display (PlayerPrefs + UI)

✔ Developed AI systems for prototypes:
  • Enemy AI using Unity DOTS/ECS for runner (performance optimization)
  • Enemy spawn system and state machine-based AI logic for top-down shooter

✔ Developed surface type detection system under vehicle wheels (raycast + layer detection) for physics and sound configuration

**Editor Tools Development and Automation:**

✔ Created localization automation tool in Google Sheets with DeepL API and Unity Localization integration:
  • Automatic translation generation for 3 projects via API
  • Translation synchronization between Google Sheets and Unity
  • Hot-reload of localization in Editor for rapid iteration

✔ Created custom Editor tool for automatic component relinking via reflection: in legacy project each vehicle bone had separate reference, tool automated this process by bone names - reduced time to add new vehicles by 10x

**Unity Analytics and Network Code:**

✔ Developed automated Selenium parser for extracting all analytics events and parameters from Unity Analytics to Google Sheets (no built-in export available)

✔ Conducted comprehensive analytics events audit: analyzed used/unused events, developed unified naming convention, renamed all events to standard

✔ Enhanced Photon synchronization network code for Offroad Outlaws Drag Racing: extended legacy logic (supported only straight-line movement) for correct synchronization on uneven maps with elevation changes

**Game Design Work:**

✔ Conducted full analysis of three products (Offroad Outlaws, No Limits Drag Racing 2, American Marksman) upon request from Battle Creek Games: compiled document with UX issues, bugs, mechanics shortcomings, and improvement recommendations

✔ Analyzed and refined game mechanics for Freeride mode, developed in-game currency earning methods and game activities

**Web Development:**

✔ Developed first version of ajika.games website: created layout (HTML/CSS), curated further improvements

---

### GD Company | Unity Developer & Lead Game Designer
**June 2021 - October 2022 (1 year 5 months)**  
**Project:** [Grand Wars](https://play.google.com/store/apps/details?id=com.gdcompany.grandwars.mafiacity) (multiplayer PvP mobile project)

Unity game systems development, game logic implementation, content integration. Additionally: Game Design (GDD, balancing, level design) and second game designer leadership.

**Unity Development:**

✔ Implemented game logic for combat events system (Cash Truck, Bank Robbery): spawn logic, AI behavior, reward system

✔ Developed dynamic character skin system with real-time switching support: hot-swap of materials and meshes without scene reload

✔ Configured character animations with weapons via Animator: stances, shooting, reloading, state transitions

✔ Performed Steel Rage project migration to new Unity version: refined all components, updated APIs, fixed breaking changes

✔ Integrated updated SDKs (Facebook, AppLovin, Firebase): ensured compatibility with new Unity version

✔ Worked on content integration and its technical implementation in Unity: prefabs setup, ScriptableObjects, configs

✔ Fixed critical bugs affecting gameplay: memory leaks, performance issues, gameplay-breaking bugs

**Game Design Work:**

✔ Developed complete set of Game Design Documents for all game features with technical specifications for developers

✔ Developed automatic weapon balance generation tool in Google Sheets with Google Apps Script: button-click item generation with full stat calculations, automatic addition to game config

✔ Balanced weapon parameters (damage, fire rate, accuracy, recoil, blast radius), character stats, economic systems

✔ Designed game map: reworked old map for new genre, increased by 2.5x, created themed zones, placed loot, configured capturable territories

✔ Developed tutorial and FTUE (First Time User Experience) for Grand Wars

**Leadership:**

✔ Mentored second game designer: assigned tasks, checked execution, provided feedback, conducted mentoring

✔ Conducted smoke and integration testing of game systems before QA handoff

---

### GD Company | QA Engineer Lead
**February 2019 - June 2021 (2 years 5 months)**  
**Projects:** Pacific Warships, Steel Rage, War After, Grand Wars (multiplayer mobile projects)

QA process organization, test documentation development, team management of 3 people. Relevant for Unity Developer: automation tools development in C# and Python.

**Automation Tools Development:**

✔ Developed comprehensive performance testing system in C# within Unity projects:
  • Automatic metrics collection (FPS, load, memory) via Profiler API
  • Data sending to Google Sheets via custom C# API for subsequent analysis
  • Automated benchmarks: algorithm for running game sessions with special camera along predetermined routes with automatic statistics collection

✔ Built debug UI in Unity with dev-tools controls: mode switching, real-time metrics visualization, quick access to frequently used functions

✔ Developed two Telegram bots in Python: automated game state cleanup via Selenium + reference database of promo codes and dev commands for all studio projects

✔ Created cross-platform application in Kivy (Python) for editing local game state files on PC and Android - simplified feature testing

✔ Automated testing process via Bash/OBS scripts: interval screen recording with automatic time marking for bug analysis

**QA and Management:**

✔ Built QA department from scratch: scaled from 1 to 3 specialists, supported three studio projects from start to release

✔ Conducted security testing: searched for exploit methods, analyzed cracked builds to identify vulnerabilities

---

## EDUCATION

**Kosygin Russian State University**  
Bachelor of Applied Mathematics and Computer Science (2013 - 2017)

**Certificates:**
- [Learn C# Course - Sololearn, 2022](https://www.sololearn.com/Certificate/CT-ZUZBDWNF/png)
- [C# Course - Codecademy, 2022](https://www.codecademy.com/profiles/daniilSlepov1798965862/certificates/65f0ff88f4fc58e0536b3b51648dff24)

**Languages:**
- **Russian** - Native
- **English** - B1 (Intermediate): technical documentation, communication with international teams

---

## SKILLS

C# • Unity • Unity DOTS • ECS • UI Toolkit • Photon • Jobs System • OOP • SOLID • Git • Plastic SCM • Jira • Visual Studio • Rider • Python • Bash • JavaScript • Google Script • AWS • CI/CD • Performance Optimization • Editor Tools • Game Design • Level Design • Agile


