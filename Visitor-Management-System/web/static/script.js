loadVisitors();
loadVisits();

document
.getElementById("visitorForm")
.addEventListener("submit", async (e) => {

    e.preventDefault();

    const data = {
        visitor_id: document.getElementById("visitor_id").value,
        name: document.getElementById("name").value,
        purpose: document.getElementById("purpose").value
    };

    await fetch("/visitor", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(data)
    });

    document.getElementById("visitorForm").reset();

    loadVisitors();
});

async function loadVisitors() {

    const response = await fetch("/visitor");
    const data = await response.json();

    let rows = "";

    data.forEach(visitor => {

        rows += `
        <tr>
            <td>${visitor.visitor_id}</td>
            <td>${visitor.name}</td>
            <td>${visitor.purpose}</td>
        </tr>
        `;
    });

    document.getElementById("visitorTable").innerHTML = rows;
}

async function loadVisits() {

    const response = await fetch("/api/visits");
    const data = await response.json();

    document.getElementById("visitCount").innerText = data.visits;
}
