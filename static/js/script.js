document.addEventListener("DOMContentLoaded", function () {

    // ---------------------------------------------
    // Resume File Count
    // ---------------------------------------------

    const resumeInput = document.getElementById("resumes");
    const fileCount = document.getElementById("file-count");

    if (resumeInput && fileCount) {

        resumeInput.addEventListener("change", function () {

            const count = resumeInput.files.length;

            if (count === 0) {
                fileCount.textContent = "No resumes selected";
            }
            else if (count === 1) {
                fileCount.textContent = "1 resume selected";
            }
            else {
                fileCount.textContent =
                    count + " resumes selected";
            }
        });
    }


    // ---------------------------------------------
    // Ranking Progress Bars
    // ---------------------------------------------

    const progressBars =
        document.querySelectorAll(".progress-bar");

    progressBars.forEach(function (bar) {

        const score =
            parseFloat(bar.dataset.score) || 0;

        const safeScore =
            Math.max(0, Math.min(score, 100));

        setTimeout(function () {
            bar.style.width = safeScore + "%";
        }, 100);
    });


    // ---------------------------------------------
    // Form Submission / Loading State
    // ---------------------------------------------

    const form = document.getElementById("rank-form");

    if (form) {

        form.addEventListener("submit", function () {

            const button =
                form.querySelector(
                    "button[type='submit']"
                );

            if (button) {

                button.disabled = true;

                button.textContent =
                    "⏳ Analyzing Resumes...";

            }
        });
    }

});