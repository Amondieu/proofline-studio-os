import fs from "node:fs";
import path from "node:path";

const root = path.resolve(process.argv[2] ?? ".");
const manifestPath = path.join(root, ".graphify", "manifest.json");

if (!fs.existsSync(manifestPath)) {
  console.error(`Graphify manifest not found: ${manifestPath}`);
  process.exit(1);
}

const manifest = JSON.parse(fs.readFileSync(manifestPath, "utf8"));
const normalized = {};

for (const [rawKey, value] of Object.entries(manifest)) {
  const windowsAbsolute = /^[A-Za-z]:[\\/]/.test(rawKey);
  const absoluteKey = windowsAbsolute || path.isAbsolute(rawKey) ? rawKey : path.resolve(root, rawKey);
  const relativeKey = path.relative(root, absoluteKey);
  if (!relativeKey || relativeKey === ".") throw new Error(`Graphify manifest contains the project root as a file key: ${rawKey}`);
  if (relativeKey === ".." || relativeKey.startsWith(`..${path.sep}`) || path.isAbsolute(relativeKey)) throw new Error(`Graphify manifest contains a path outside the project root: ${rawKey}`);
  normalized[relativeKey.split(path.sep).join("/")] = value;
}

fs.writeFileSync(manifestPath, `${JSON.stringify(normalized, null, 2)}\n`, "utf8");
console.log(`Normalized Graphify manifest paths: ${Object.keys(normalized).length} file(s).`);
