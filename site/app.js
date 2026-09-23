const directionData = {
  precision: { number: "01", label: "Precision System", eyebrow: "PRECISION SYSTEM / 01", title: "Complexity becomes a clear decision system.", body: "Structured, calm, and exact. A visual language for offers where trust is earned through clarity.", cta: "Request a Precision sprint", motion: "SIGNAL GRID" },
  cinematic: { number: "02", label: "Cinematic Authority", eyebrow: "CINEMATIC AUTHORITY / 02", title: "Your offer deserves a stage, not another page.", body: "Bold, memorable, and controlled. A visual language for launches people remember.", cta: "Request a Cinematic sprint", motion: "SCULPTURAL OBJECT" },
  editorial: { number: "03", label: "Editorial Luxury", eyebrow: "EDITORIAL LUXURY / 03", title: "Clarity is the ultimate luxury.", body: "Quiet, tactile, and considered. A visual language for premium services where trust is earned through restraint.", cta: "Request an Editorial sprint", motion: "EDITORIAL LIGHT" }
};

const root = document.documentElement;
const buttons = document.querySelectorAll("[data-direction-choice]");
const stageLabel = document.querySelector("#stage-label");
const previewEyebrow = document.querySelector("#preview-eyebrow");
const previewTitle = document.querySelector("#preview-title");
const previewBody = document.querySelector("#preview-body");
const directionCta = document.querySelector("#direction-cta");
const artDirection = document.querySelector("#art-direction");

function setDirection(id) {
  const data = directionData[id];
  if (!data) return;
  root.dataset.direction = id;
  localStorage.setItem("proofline-direction", id);
  buttons.forEach((button) => {
    const active = button.dataset.directionChoice === id;
    button.classList.toggle("is-active", active);
    button.setAttribute("aria-pressed", String(active));
  });
  stageLabel.textContent = `${id.toUpperCase()} / ${data.number}`;
  previewEyebrow.textContent = data.eyebrow;
  previewTitle.textContent = data.title;
  previewBody.textContent = data.body;
  directionCta.firstChild.textContent = `${data.cta} `;
  artDirection.textContent = data.motion;
}

buttons.forEach((button) => button.addEventListener("click", () => setDirection(button.dataset.directionChoice)));
setDirection(localStorage.getItem("proofline-direction") || "precision");

document.querySelector("#teardown-form").addEventListener("submit", (event) => {
  event.preventDefault();
  const form = event.currentTarget;
  const status = document.querySelector("#form-status");
  const selected = directionData[root.dataset.direction];
  status.textContent = `Demo received. Your request is tagged ${selected.label}; no data was sent from this concept site.`;
  form.reset();
});
