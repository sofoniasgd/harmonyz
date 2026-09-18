// Site content lives here. To publish a change (a new project, a new job, a new
// certification) edit this file and re-upload just this one file to shared
// hosting -- no rebuild of output.css and no repackaging the rest of the site.

// --- Projects -----------------------------------------------------------
// image is optional: leave it "" and the card will show an "add project
// image" placeholder instead of a broken image. liveUrl / githubUrl are
// optional too -- leave either "" to hide that link on the card.
const projects = [
  {
    title: "Project Title",
    description: "One or two sentence summary of what this project does and the problem it solves.",
    tags: ["Tech", "Stack", "Here"],
    image: "",
    liveUrl: "",
    githubUrl: ""
  },
    {
    title: "Project Title",
    description: "One or two sentence summary of what this project does and the problem it solves.",
    tags: ["Tech", "Stack", "Here"],
    image: "",
    liveUrl: "",
    githubUrl: ""
  },
    {
    title: "Project Title",
    description: "One or two sentence summary of what this project does and the problem it solves.",
    tags: ["Tech", "Stack", "Here"],
    image: "",
    liveUrl: "",
    githubUrl: ""
  }
];

// --- Hero -------------------------------------------------------------
// Titles typed one by one in a loop under the name on the hero section.
// Add, remove, or reorder entries here -- no index.html edit needed.
const heroTitles = ["Software Engineer", "IT Technician"];

// --- About ----------------------------------------------------------------
const aboutBio = "Backend-leaning full-stack engineer who also handles systems & IT support — from writing the API to keeping the server it runs on healthy.";

// SVG markup for each skill icon, keyed by name. A skill's `icon` field below
// just has to match one of these keys -- reuse an existing key, or add a new
// key here with your own inline SVG to introduce a brand-new icon. Either
// way, no index.html edit needed. Unknown keys fall back to `generic`.
const skillIcons = {
  python: `<svg viewBox="0 0 128 128" class="w-7 h-7 flex-shrink-0">
    <linearGradient id="py-a" x1="70.252" x2="170.659" y1="1237.476" y2="1151.089" gradientTransform="matrix(.563 0 0 -.568 -29.215 707.817)" gradientUnits="userSpaceOnUse">
      <stop offset="0" stop-color="#5A9FD4"/><stop offset="1" stop-color="#306998"/>
    </linearGradient>
    <linearGradient id="py-b" x1="209.474" x2="173.62" y1="1098.811" y2="1149.537" gradientTransform="matrix(.563 0 0 -.568 -29.215 707.817)" gradientUnits="userSpaceOnUse">
      <stop offset="0" stop-color="#FFD43B"/><stop offset="1" stop-color="#FFE873"/>
    </linearGradient>
    <path fill="url(#py-a)" d="M63.391 1.988c-4.222.02-8.252.379-11.8 1.007-10.45 1.846-12.346 5.71-12.346 12.837v9.411h24.693v3.137H29.977c-7.176 0-13.46 4.313-15.426 12.521-2.268 9.405-2.368 15.275 0 25.096 1.755 7.311 5.947 12.519 13.124 12.519h8.491V67.234c0-8.151 7.051-15.34 15.426-15.34h24.665c6.866 0 12.346-5.654 12.346-12.548V15.833c0-6.693-5.646-11.72-12.346-12.837-4.244-.706-8.645-1.027-12.866-1.008zM50.037 9.557c2.55 0 4.634 2.117 4.634 4.721 0 2.593-2.083 4.69-4.634 4.69-2.56 0-4.633-2.097-4.633-4.69-.001-2.604 2.073-4.721 4.633-4.721z" transform="translate(0 10.26)"/>
    <path fill="url(#py-b)" d="M91.682 28.38v10.966c0 8.5-7.208 15.655-15.426 15.655H51.591c-6.756 0-12.346 5.783-12.346 12.549v23.515c0 6.691 5.818 10.628 12.346 12.547 7.816 2.297 15.312 2.713 24.665 0 6.216-1.801 12.346-5.423 12.346-12.547v-9.412H63.938v-3.138h37.012c7.176 0 9.852-5.005 12.348-12.519 2.578-7.735 2.467-15.174 0-25.096-1.774-7.145-5.161-12.521-12.348-12.521h-9.268zM77.809 87.927c2.561 0 4.634 2.097 4.634 4.692 0 2.602-2.074 4.719-4.634 4.719-2.55 0-4.633-2.117-4.633-4.719 0-2.595 2.083-4.692 4.633-4.692z" transform="translate(0 10.26)"/>
  </svg>`,

  javascript: `<svg viewBox="0 0 128 128" class="w-7 h-7 flex-shrink-0">
    <path fill="#F0DB4F" d="M1.408 1.408h125.184v125.185H1.408z"/>
    <path fill="#323330" d="M116.347 96.736c-.917-5.711-4.641-10.508-15.672-14.981-3.832-1.761-8.104-3.022-9.377-5.926-.452-1.69-.512-2.642-.226-3.665.821-3.32 4.784-4.355 7.925-3.403 2.023.678 3.938 2.237 5.093 4.724 5.402-3.498 5.391-3.475 9.163-5.879-1.381-2.141-2.118-3.129-3.022-4.045-3.249-3.629-7.676-5.498-14.756-5.355l-3.688.477c-3.534.893-6.902 2.748-8.877 5.235-5.926 6.724-4.236 18.492 2.975 23.335 7.104 5.332 17.54 6.545 18.873 11.531 1.297 6.104-4.486 8.08-10.234 7.378-4.236-.881-6.592-3.034-9.139-6.949-4.688 2.713-4.688 2.713-9.508 5.485 1.143 2.499 2.344 3.63 4.26 5.795 9.068 9.198 31.76 8.746 35.83-5.176.165-.478 1.261-3.666.38-8.581zM69.462 58.943H57.753l-.048 30.272c0 6.438.333 12.34-.714 14.149-1.713 3.558-6.152 3.117-8.175 2.427-2.059-1.012-3.106-2.451-4.319-4.485-.333-.584-.583-1.036-.667-1.071l-9.52 5.83c1.583 3.249 3.915 6.069 6.902 7.901 4.462 2.678 10.459 3.499 16.731 2.059 4.082-1.189 7.604-3.652 9.448-7.401 2.666-4.915 2.094-10.864 2.07-17.444.06-10.735.001-21.468.001-32.237z"/>
  </svg>`,

  mysql: `<svg viewBox="0 0 128 128" class="w-7 h-7 flex-shrink-0">
    <path fill="#e6f4f1" d="M116.948 97.807c-6.863-.187-12.104.452-16.585 2.341-1.273.537-3.305.552-3.513 2.147.7.733.809 1.829 1.365 2.731 1.07 1.73 2.876 4.052 4.488 5.268 1.762 1.33 3.577 2.751 5.465 3.902 3.358 2.047 7.107 3.217 10.34 5.268 1.906 1.21 3.799 2.733 5.658 4.097.92.675 1.537 1.724 2.732 2.147v-.194c-.628-.8-.79-1.898-1.366-2.733l-2.537-2.537c-2.48-3.292-5.629-6.184-8.976-8.585-2.669-1.916-8.642-4.504-9.755-7.609l-.195-.195c1.892-.214 4.107-.898 5.854-1.367 2.934-.786 5.556-.583 8.585-1.365l4.097-1.171v-.78c-1.531-1.571-2.623-3.651-4.292-5.073-4.37-3.72-9.138-7.437-14.048-10.537-2.724-1.718-6.089-2.835-8.976-4.292-.971-.491-2.677-.746-3.318-1.562-1.517-1.932-2.342-4.382-3.511-6.633-2.449-4.717-4.854-9.868-7.024-14.831-1.48-3.384-2.447-6.72-4.293-9.756-8.86-14.567-18.396-23.358-33.169-32-3.144-1.838-6.929-2.563-10.929-3.513-2.145-.129-4.292-.26-6.438-.391-1.311-.546-2.673-2.149-3.902-2.927C17.811 4.565 5.257-2.16 1.633 6.682c-2.289 5.581 3.421 11.025 5.462 13.854 1.434 1.982 3.269 4.207 4.293 6.438.674 1.467.79 2.938 1.367 4.489 1.417 3.822 2.652 7.98 4.487 11.511.927 1.788 1.949 3.67 3.122 5.268.718.981 1.951 1.413 2.145 2.927-1.204 1.686-1.273 4.304-1.95 6.44-3.05 9.615-1.899 21.567 2.537 28.683 1.36 2.186 4.567 6.871 8.975 5.073 3.856-1.57 2.995-6.438 4.098-10.732.249-.973.096-1.689.585-2.341v.195l3.513 7.024c2.6 4.187 7.212 8.562 11.122 11.514 2.027 1.531 3.623 4.177 6.244 5.073v-.196h-.195c-.508-.791-1.303-1.119-1.951-1.755-1.527-1.497-3.225-3.358-4.487-5.073-3.556-4.827-6.698-10.11-9.561-15.609-1.368-2.627-2.557-5.523-3.709-8.196-.444-1.03-.438-2.589-1.364-3.122-1.263 1.958-3.122 3.542-4.098 5.854-1.561 3.696-1.762 8.204-2.341 12.878-.342.122-.19.038-.391.194-2.718-.655-3.672-3.452-4.683-5.853-2.554-6.07-3.029-15.842-.781-22.829.582-1.809 3.21-7.501 2.146-9.172-.508-1.666-2.184-2.63-3.121-3.903-1.161-1.574-2.319-3.646-3.124-5.464-2.09-4.731-3.066-10.044-5.267-14.828-1.053-2.287-2.832-4.602-4.293-6.634-1.617-2.253-3.429-3.912-4.683-6.635-.446-.968-1.051-2.518-.391-3.513.21-.671.508-.951 1.171-1.17 1.132-.873 4.284.29 5.462.779 3.129 1.3 5.741 2.538 8.392 4.294 1.271.844 2.559 2.475 4.097 2.927h1.756c2.747.631 5.824.195 8.391.975 4.536 1.378 8.601 3.523 12.292 5.854 11.246 7.102 20.442 17.21 26.732 29.269 1.012 1.942 1.45 3.794 2.341 5.854 1.798 4.153 4.063 8.426 5.852 12.488 1.786 4.052 3.526 8.141 6.05 11.513 1.327 1.772 6.451 2.723 8.781 3.708 1.632.689 4.307 1.409 5.854 2.34 2.953 1.782 5.815 3.903 8.586 5.855 1.383.975 5.64 3.116 5.852 4.879zM29.729 23.466c-1.431-.027-2.443.156-3.513.389v.195h.195c.683 1.402 1.888 2.306 2.731 3.513.65 1.367 1.301 2.732 1.952 4.097l.194-.193c1.209-.853 1.762-2.214 1.755-4.294-.484-.509-.555-1.147-.975-1.755-.556-.811-1.635-1.272-2.339-1.952z"/>
  </svg>`,

  flask: `<svg viewBox="0 0 128 128" class="w-7 h-7 flex-shrink-0">
    <path fill="#e6f4f1" d="M44.44 100.63c-4.23-3.33-8.74-6.52-11.83-11.01-6.49-7.92-11.49-17.1-14.9-26.74-2.07-6.27-2.77-12.99-5.44-19.02-2.78-4.38.48-9.16 5.27-10.55 2.13-.41 5.89-2.43 1.36-.98-4.06 2.98-4.45-2.71-.29-3.07 2.84-.38 3.89-2.7 2.92-4.8-3.05-1.99 7.4-4.18 2.14-7.15-5.48-5.91 7.66-7.05 4.42-.33-.77 5.16 9.18-.95 6.87 5.01 2.35 2.86 8.8.65 8.63 4.67 3.42.24 4.6 3.11 7.8 3.33 3.33 1.5 9.36 2.69 10.49 6.44-3.3 2.61-10.95-5.4-11.31 1.84 1 10.69.74 21.7 4.65 31.88 1.85 6.16 6.33 11.01 10.38 15.81 3.88 4.7 9.12 8.01 14.48 10.8 4.69 2.21 9.75 3.68 14.87 4.6 2.07-1.59 5.74-7.48 8.97-5 .16 2.8-6.42 5.84-.31 5.54 3.59-1.08 6.08 2.77 9.04-.71 2.72 3.23 11.32-2.06 9.38 4.53-2.62 1.69-6.44.67-9.07 3-4.33-2.16-7.77 1.93-12.56 1.42-5.32.95-10.73 1.34-16.13 1.34-8.85-.7-17.89-.99-26.3-4.07-4.74-1.38-9.37-4.08-13.53-6.78z"/>
  </svg>`,

  nodejs: `<svg viewBox="0 0 128 128" class="w-7 h-7 flex-shrink-0">
    <path fill="#83CD29" d="M112.771 30.334 68.674 4.729c-2.781-1.584-6.402-1.584-9.205 0L14.901 30.334C12.031 31.985 10 35.088 10 38.407v51.142c0 3.319 2.084 6.423 4.954 8.083l11.775 6.688c5.628 2.772 7.617 2.772 10.178 2.772 8.333 0 13.093-5.039 13.093-13.828v-50.49c0-.713-.371-1.774-1.071-1.774h-5.623C42.594 41 41 42.061 41 42.773v50.49c0 3.896-3.524 7.773-10.11 4.48L18.723 90.73c-.424-.23-.723-.693-.723-1.181V38.407c0-.482.555-.966.982-1.213l44.424-25.561c.415-.235 1.025-.235 1.439 0l43.882 25.555c.42.253.272.722.272 1.219v51.142c0 .488.183.963-.232 1.198l-44.086 25.576c-.378.227-.847.227-1.261 0l-11.307-6.749c-.341-.198-.746-.269-1.073-.086-3.146 1.783-3.726 2.02-6.677 3.043-.726.253-1.797.692.41 1.929l14.798 8.754a9.294 9.294 0 0 0 4.647 1.246c1.642 0 3.25-.426 4.667-1.246l43.885-25.582c2.87-1.672 4.23-4.764 4.23-8.083V38.407c0-3.319-1.36-6.414-4.229-8.073zM77.91 81.445c-11.726 0-14.309-3.235-15.17-9.066-.1-.628-.633-1.379-1.272-1.379h-5.731c-.709 0-1.279.86-1.279 1.566 0 7.466 4.059 16.512 23.453 16.512 14.039 0 22.088-5.455 22.088-15.109 0-9.572-6.467-12.084-20.082-13.886-13.762-1.819-15.16-2.738-15.16-5.962 0-2.658 1.184-6.203 11.374-6.203 9.105 0 12.461 1.954 13.842 8.091.118.577.645.991 1.24.991h5.754c.354 0 .692-.143.94-.396.24-.272.367-.613.335-.979-.891-10.568-7.912-15.493-22.112-15.493-12.631 0-20.166 5.334-20.166 14.275 0 9.698 7.497 12.378 19.622 13.577 14.505 1.422 15.633 3.542 15.633 6.395 0 4.955-3.978 7.066-13.309 7.066z"/>
  </svg>`,

  html5: `<svg viewBox="0 0 128 128" class="w-7 h-7 flex-shrink-0">
    <path fill="#E44D26" d="M19.037 113.876 9.032 1.661h109.936l-10.016 112.198-45.019 12.48z"/>
    <path fill="#F16529" d="m64 116.8 36.378-10.086 8.559-95.878H64z"/>
    <path fill="#EBEBEB" d="M64 52.455H45.788L44.53 38.361H64V24.599H29.489l.33 3.692 3.382 37.927H64zm0 35.743-.061.017-15.327-4.14-.979-10.975H33.816l1.928 21.609 28.193 7.826.063-.017z"/>
    <path fill="#fff" d="M63.952 52.455v13.763h16.947l-1.597 17.849-15.35 4.143v14.319l28.215-7.82.207-2.325 3.234-36.233.335-3.696h-3.708zm0-27.856v13.762h33.244l.276-3.092.628-6.978.329-3.692z"/>
  </svg>`,

  tailwind: `<svg viewBox="0 0 128 128" class="w-7 h-7 flex-shrink-0">
    <path fill="#38bdf8" d="M64.004 25.602c-17.067 0-27.73 8.53-32 25.597 6.398-8.531 13.867-11.73 22.398-9.597 4.871 1.214 8.352 4.746 12.207 8.66C72.883 56.629 80.145 64 96.004 64c17.066 0 27.73-8.531 32-25.602-6.399 8.536-13.867 11.735-22.399 9.602-4.87-1.215-8.347-4.746-12.207-8.66-6.27-6.367-13.53-13.738-29.394-13.738zM32.004 64c-17.066 0-27.73 8.531-32 25.602C6.402 81.066 13.87 77.867 22.402 80c4.871 1.215 8.352 4.746 12.207 8.66 6.274 6.367 13.536 13.738 29.395 13.738 17.066 0 27.73-8.53 32-25.597-6.399 8.531-13.867 11.73-22.399 9.597-4.87-1.214-8.347-4.746-12.207-8.66C55.128 71.371 47.868 64 32.004 64zm0 0"/>
  </svg>`,

  alpine: `<svg viewBox="0 0 128 128" class="w-7 h-7 flex-shrink-0">
    <path fill="#77c1d2" fill-rule="evenodd" d="M98.444 35.562 126 62.997 98.444 90.432 70.889 62.997z" clip-rule="evenodd"/>
    <path fill="#8fa8a4" fill-rule="evenodd" d="m29.556 35.562 57.126 56.876H31.571L2 62.997z" clip-rule="evenodd"/>
  </svg>`,

  react: `<svg viewBox="0 0 128 128" class="w-7 h-7 flex-shrink-0">
    <g fill="#61DAFB">
      <circle cx="64" cy="64" r="11.4"/>
      <path d="M107.3 45.2c-2.2-.8-4.5-1.6-6.9-2.3.6-2.4 1.1-4.8 1.5-7.1 2.1-13.2-.2-22.5-6.6-26.1-1.9-1.1-4-1.6-6.4-1.6-7 0-15.9 5.2-24.9 13.9-9-8.7-17.9-13.9-24.9-13.9-2.4 0-4.5.5-6.4 1.6-6.4 3.7-8.7 13-6.6 26.1.4 2.3.9 4.7 1.5 7.1-2.4.7-4.7 1.4-6.9 2.3C8.2 50 1.4 56.6 1.4 64s6.9 14 19.3 18.8c2.2.8 4.5 1.6 6.9 2.3-.6 2.4-1.1 4.8-1.5 7.1-2.1 13.2.2 22.5 6.6 26.1 1.9 1.1 4 1.6 6.4 1.6 7.1 0 16-5.2 24.9-13.9 9 8.7 17.9 13.9 24.9 13.9 2.4 0 4.5-.5 6.4-1.6 6.4-3.7 8.7-13 6.6-26.1-.4-2.3-.9-4.7-1.5-7.1 2.4-.7 4.7-1.4 6.9-2.3 12.5-4.8 19.3-11.4 19.3-18.8s-6.8-14-19.3-18.8z"/>
    </g>
  </svg>`,

  // Shown for any skill whose `icon` key isn't listed above, so a typo or a
  // not-yet-illustrated skill still renders something instead of nothing.
  generic: `<svg viewBox="0 0 24 24" fill="none" class="w-7 h-7 flex-shrink-0 text-text-dim">
    <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="m8 7-5 5 5 5m8-10 5 5-5 5"/>
  </svg>`
};

// icon must match a key in skillIcons above (or add a new key there).
// percent is 0-100 and drives the animated skill bar.
const skills = [
  { name: "Python", level: "Advanced", percent: 80, icon: "python" },
  { name: "JavaScript", level: "Familiar", percent: 40, icon: "javascript" },
  { name: "MySQL", level: "Intermediate", percent: 60, icon: "mysql" },
  { name: "Flask", level: "Intermediate", percent: 60, icon: "flask" },
  { name: "Node.js", level: "Familiar", percent: 40, icon: "nodejs" },
  { name: "HTML5", level: "Intermediate", percent: 60, icon: "html5" },
  { name: "Tailwind CSS", level: "Familiar", percent: 40, icon: "tailwind" },
  { name: "Alpine.js", level: "Familiar", percent: 40, icon: "alpine" },
  { name: "React", level: "Familiar", percent: 40, icon: "react" }
];

const powerPlatform = [
  {
    title: "Apps & Automation",
    items: [
      "Power Apps Studio (Canvas & Model-Driven Apps)",
      "Power Automate (Cloud & Desktop Flows)"
    ]
  },
  {
    title: "Data & Collaboration",
    items: [
      "Dataverse Management",
      "SharePoint Administration"
    ]
  }
];

const itSolutions = [
  {
    title: "Systems & Infrastructure",
    items: [
      "Windows & Linux Administration",
      "Virtualization",
      "Cloud & Hosting Management",
      "System Performance Monitoring & Optimization"
    ]
  },
  {
    title: "Networking & Security",
    items: [
      "Network Configuration & Troubleshooting",
      "Basic Firewall & Security Setup",
      "VPN & Remote Access Configuration",
      "Domain & DNS Management"
    ]
  },
  {
    title: "Hardware & Troubleshooting",
    items: [
      "PC & Server Maintenance",
      "Hardware Diagnostics & Repair",
      "Storage & Backup Solutions",
      "Peripheral & Device Setup"
    ]
  },
  {
    title: "IT Support & Operations",
    items: [
      "Software Installation & Configuration",
      "Technical Support & Issue Resolution",
      "IT Documentation & Process Automation",
      "End-User Training & Assistance"
    ]
  }
];

// --- Experience -----------------------------------------------------------
const experience = [
  {
    role: "Software Engineer",
    org: "Addis Ababa (Freelance)",
    period: "2024 — Present",
    summary: "Building full-stack web applications and backend services for freelance clients."
  },
  {
    role: "Database Administrator",
    org: "A.A. City Administration",
    period: "2022 — Present",
    summary: "Managing and maintaining production databases and data integrity for city administration systems."
  },
  {
    role: "IT Maintenance Specialist",
    org: "Addis Ababa (Freelance)",
    period: "2021 — Present",
    summary: "Providing IT support, systems maintenance, and infrastructure troubleshooting."
  },
  {
    role: "Power Platform Developer",
    org: "Addis Ababa (Remote)",
    period: "2025 — Present",
    summary: "Power Apps Studio, Power Automation, Dataverse Management, Sharepoint Administration"
  }
];

// --- Education -----------------------------------------------------------
const education = [
  {
    program: "Software Engineering (Backend Specialization)",
    school: "ALX",
    period: "2023 — 2024"
  },
  {
    program: "Electrical and Computer Engineering (BSc)",
    school: "Adigrat University, Ethiopia",
    period: "2014 — 2019"
  },
  {
    program: "High School Diploma",
    school: "Bashewam High School, Ethiopia",
    period: "2008 — 2013"
  }
];
