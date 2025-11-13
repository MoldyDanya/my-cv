# DANIIL SLEPOV

<img src="https://github.com/MoldyDanya.png" width="150" align="right" style="border-radius: 50%; margin-left: 20px;">

**DevOps Engineer (GameDev)**

**Email:** dev@dslepov.ru | **Telegram:** @MoldyDanya | **Phone:** +7 (905) 775-02-90  
**Location:** Moscow, Russia | **Work Format:** Remote (not open to relocation or business trips)

---

## ABOUT ME

DevOps Engineer with experience in game development (Unity mobile projects).

Worked for a year as DevOps Engineer on Unity mobile projects in an international team: built AWS infrastructure from scratch, configured CI/CD pipeline, reduced build time from 1+ hour to 30-40 minutes, deployment from 2+ hours to 50-60 minutes, reduced failed builds by 80%, optimized costs through custom caching and on-demand provisioning.

Before DevOps, spent almost 4 years combining Unity Developer / Game Designer roles (prototyping, game design, UI, systems) and 2+ years as QA Lead (processes, automation, performance testing, security testing). Understand game development specifics from the inside and easily adapt to different engines and CI/CD systems - the main thing is solving team challenges.

Not afraid to make decisions, take responsibility, and drive tasks from start to finish. Ready to tackle complex challenges, adapt quickly, and implement best practices.

**Real CI/CD automation examples** (GitHub Actions workflows, Fastlane deployment configs) in my portfolio: https://github.com/MoldyDanya/devops-portfolio

**Comprehensive resume with full work experience** (Unity Development, Game Design, DevOps, QA, team management): [master-cv-en.md](https://github.com/MoldyDanya/my-cv/blob/main/master-cv-en.md)

---

## KEY SKILLS

**DevOps and Cloud Technologies**  
AWS EC2, AMI snapshots, on-demand provisioning, monitoring (Grafana, AWS CloudWatch, Prometheus), alerting (Slack), incident management, Docker, Docker Compose

**CI/CD Automation**  
GitHub Actions (multi-trigger workflows: manual/scheduled/automated), modular and reusable workflows, custom Unity build caching, semantic versioning via git tags, Fastlane (automated deployment to Google Play and TestFlight)

**Unity and Game Development**  
C#, Unity Editor, project upgrades to new Unity versions (including major updates), SDK integration (Facebook, AppLovin, Firebase), understanding of mobile game development specifics

**Testing and QA Automation**  
AltTester (CI/CD integration for Unity UI testing), automated testing, performance testing, security testing

**Tools and Processes**  
Git, Plastic SCM, Jira, Trello, Bash, Python, Ruby, JavaScript, technical leadership, process documentation

---

## WORK EXPERIENCE

### Ajika Games | DevOps Engineer (Unity Mobile Projects)
**November 2024 - September 2025 (11 months)**  
Location: China (remote) | Format: Outstaffing for Battle Creek Games projects  
**Projects:** [Offroad Outlaws](https://play.google.com/store/apps/details?id=com.battlecreek.offroadoutlaws), [No Limit Drag Racing 2](https://play.google.com/store/apps/details?id=com.battlecreek.nolimit2)

Worked as DevOps Engineer on two Unity mobile projects (Android/iOS). Full DevOps cycle: AWS infrastructure design, CI/CD pipeline management, automated testing integration, coordination between Dev, QA and release processes.

**Cloud Infrastructure (AWS):**

✔ Designed scalable AWS infrastructure for specific requirements: selected CPU-optimized instances for fast builds, GPU instance for automated UI testing, development server - each chosen based on performance and cost criteria

✔ Administered 4 EC2 servers in production (2 CPU for builds, 1 GPU for UI tests, 1 dev), ensured >99% uptime

✔ Implemented on-demand provisioning with automatic startup before build and shutdown on idle timer - eliminated payment for idle resources and optimized performance-to-cost ratio

✔ Created and maintained AMI snapshots when making server changes for quick recovery in case of incidents

✔ Set up comprehensive monitoring via Grafana and AWS CloudWatch with Prometheus integration for metrics collection

✔ Implemented automated Slack alerts system for proactive problem detection and downtime minimization

**CI/CD Automation (GitHub Actions):**

✔ Developed modular GitHub Actions workflows with logic encapsulation: project code changes and CI/CD didn't affect each other, maintained flexible multi-trigger system (manual/scheduled/auto-test triggers)

✔ Configured fully automated deployment via Fastlane:
  • Android → Google Play with track selection (Internal/Beta/Production)
  • iOS → TestFlight via Xcode on macOS GitHub-hosted runners

✔ Created user-friendly workflow interface with clear parameters for one-click builds/deployments

✔ Developed custom Unity build caching system under budget constraints for significant reduction in GitHub Actions minutes

✔ Implemented semantic versioning system via git tags with automatic version increments for reliable deployment tracking

**Incident Management and Unity Integration:**

✔ Integrated AltTester UI testing with GPU server (Xvfb, Openbox, OpenGL, NVIDIA Driver) into CI/CD pipeline

✔ Conducted deep root cause analysis of every failed build and documented preventive measures - reduced failing builds by 80%

✔ Ensured safe upgrade of two projects from Unity 2022.3.40 to Unity 6000.1.11 (major version) without CI/CD downtime: updated APIs, fixed breaking changes, refined components, integrated updated SDKs (Facebook, AppLovin, Firebase) - avoided release cycle disruption

**Communication and Leadership:**

✔ Established transparent communication between Dev and QA through automatic builds - QA team gained ability to test features on the day of commit

✔ Fostered culture of responsibility for build quality: trained developers to work with pipelines and versioning logic, explained infrastructure principles to new employees

✔ Conducted regular discussions with technical director, leads, and client on CI/CD architecture decisions, gathered developer feedback and implemented improvements based on real needs

**Key Results:**

✔ Reduced build time from 1+ hour to 30-40 minutes, deployment from 2+ hours to 50-60 minutes

✔ Fully automated delivery pipeline from commit to TestFlight/Google Play - eliminated need for manual operations

✔ Ensured infrastructure uptime of 99%+, reduced recurring incidents through preventive documentation

---

### Ajika Games | Unity Developer / Game Designer
**November 2022 - November 2024 (2 years 1 month)**  
Location: China (remote)  
**Projects:** Prototypes + multiplayer mobile projects (Offroad Outlaws, No Limits Drag Racing 2, Offroad Outlaws Drag Racing, American Marksman)

Game design and game systems development, prototyping, automation tools integration, Unity Analytics implementation, UI Toolkit, localization, network code (Photon).

**Key Results:**

✔ Developed innovative puzzle game prototype (untangling planar graphs) - created complete Game Design Document, visual editor for graph creation, balancing tools, built UI with UI Toolkit, coordinated team (Unity dev, UI artist, VFX dev)

✔ Implemented realistic vehicle systems for racing project: motorcycle stabilization, ski and track system for snowmobiles via raycast with Jobs optimization, dynamic suspension, headlight system, vehicle deformation

✔ Developed localization automation tool (Unity Localization + DeepL + Google Translate) for three projects - localization stopped being a bottleneck

✔ Created tool for automatic component relinking via reflection - accelerated prefab setup and new developer onboarding

✔ Worked with Unity Analytics: created analytics events, refactored naming, developed event parser (Selenium) for legacy event analysis and further refactoring

✔ Developed AI systems for enemy behavior management in prototypes (DOTS, state machine)

---

### GD Company | Unity Developer / Game Designer
**June 2021 - October 2022 (1 year 5 months)**  
**Project:** Grand Wars (multiplayer PvP mobile project)

Game design, game systems and content balance development, Unity development, mechanics integration into multiplayer product.

**Key Results:**

✔ Developed Game Design Documents for Grand Wars features, designed game map considering balance and player experience

✔ Created automatic weapon balance generation system (Google Sheets + Google Apps Script) - features launched faster without manual editing

✔ Balanced weapon parameters, character stats, and economic systems, interpreted analytics to optimize player experience

✔ Implemented game logic for combat events system and dynamic character skin system with real-time switching support

✔ Performed Steel Rage migration to new Unity version with refinements and updated SDK integration

---

### GD Company | QA Engineer Lead
**February 2019 - June 2021 (2 years 5 months)**  
**Projects:** Pacific Warships, Steel Rage, War After, Grand Wars (multiplayer mobile projects)

QA process organization and leadership from scratch, test documentation development, team management of 3 people, test automation, security testing for multiplayer projects.

**Key Results:**

✔ Built QA department from scratch - from single specialist grew to team of 3 with clear processes, supported three studio projects from start to release

✔ Developed complete set of test documentation: test suites, cases, and checklists for regression and functional testing

✔ Distributed tasks among QA staff, controlled execution, mentored newcomers, conducted interviews and was responsible for hiring

✔ Developed automated performance testing system within project (C#, Python, OBS scripts) - routine checks automated

✔ Conducted security testing: searched for exploit methods, analyzed cracked builds to identify vulnerabilities and implement fixes

✔ Created two Telegram bots: automated game state cleanup via Selenium + reference database of promo codes/dev commands

✔ Developed cross-platform application in Kivy (Python) for editing game state files on PC and Android

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

C# • Python • Bash • Ruby • JavaScript • Git • Plastic SCM • Jira • Trello • Unity • Unity DOTS • Photon • AWS EC2 • Docker • Docker Compose • GitHub Actions • Fastlane • Terraform • Linux • macOS • Android • iOS • Firebase • Prometheus • Grafana • CI/CD • DevOps • Process Automation


