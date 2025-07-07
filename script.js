
const map = L.map('map').setView([46.5, 2.2], 6);
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png').addTo(map);

// Exemple de cercle sur Paris
const zone = L.circle([48.8566, 2.3522], { radius: 50000, color: '#3388ff' }).addTo(map);
zone.on('click', async () => {
    const name = prompt("Nom de l'agent:");
    const photo = prompt("URL de la photo:");
    if (!name) return;
    const payload = { "zone_paris": { name, photo } };
    await fetch("/api/assign", {
        method: "POST",
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(payload)
    });
    alert("Agent assigné !");
});
