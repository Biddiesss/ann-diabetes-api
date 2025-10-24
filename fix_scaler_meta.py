import json

# Read the current scaler metadata
with open("model/scaler_meta.json", "r") as f:
    meta = json.load(f)

# Remove 'Outcome' from feature_names if it exists
if "Outcome" in meta["feature_names"]:
    meta["feature_names"].remove("Outcome")
    print("Removed 'Outcome' from feature_names")

# Display the corrected metadata
print("\nCorrected metadata:")
print(f"Number of features: {len(meta['feature_names'])}")
print(f"Feature names: {meta['feature_names']}")
print(f"Mean values: {len(meta['mean'])} values")
print(f"Scale values: {len(meta['scale'])} values")

# Save the corrected metadata
with open("model/scaler_meta.json", "w") as f:
    json.dump(meta, f, indent=2)

print("\n✓ Scaler metadata fixed and saved!")