
// static/scripts/table.js
const csrfMeta = document.querySelector('meta[name="csrf-token"]');
export function initTable() {


  
  const csrfToken = csrfMeta ? csrfMeta.content : "";

  const table = document.querySelector("table");
  if (!table) return console.warn("No table element found");

  // 🔹 Save button logic
  table.querySelectorAll(".save-btn").forEach((btn) => {
    btn.addEventListener("click", async (e) => {
      const row = e.target.closest("tr");
      const studentId = row.dataset.studentId;
      const name = row.querySelector("td:nth-child(1) input").value;
      const age = row.querySelector("td:nth-child(2) input").value;
      const english = row.querySelector('[data-subject="english"]').value;
      const math = row.querySelector('[data-subject="math"]').value;

      try {
        const res = await fetch(`/update_student/${studentId}`, {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
            "X-CSRFToken": csrfToken,
          },
          body: JSON.stringify({ name, age, english, math }),
        });

        if (res.ok) {
          const data = await res.json();
          row.querySelector("td:nth-child(5) input").value = data.grade;
          row.style.backgroundColor = "#d4edda";
          setTimeout(() => (row.style.backgroundColor = ""), 1000);
        } else {
          alert("Failed to update student!");
        }
      } catch (err) {
        console.error("Error updating student:", err);
      }
    });
  });

  // 🔹 Delete button logic
  table.querySelectorAll(".delete-btn").forEach((btn) => {
    btn.addEventListener("click", async (e) => {
      const row = e.target.closest("tr");
      const studentId = row.dataset.studentId;

      if (!confirm("Are you sure you want to delete this student?")) return;

      try {
        const response = await fetch(`/delete_student/${studentId}`, {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
            "X-CSRFToken": csrfToken,
          },
        });

        if (response.ok) {
          row.remove();
          alert("Student deleted successfully!");
        } else {
          alert("Failed to delete student.");
        }
      } catch (err) {
        console.error("Error deleting student:", err);
      }
    });
  });
}
