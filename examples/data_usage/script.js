/**
 *
 * (c) 2024 Pedro L Dias
 *
 * This file is a demonstration of the use of questions extracted by enem-extractor
 * learn more at https://github.com/diaslui/enem-extractor
 */

let quizData = [];
let maxScore = 0;
let currentQuestionIndex = 0;
let score = 0;
let timerInterval;

const quizContent = document.getElementById("quiz-content");
const quizAlternatives = document.getElementById("alternatives");
const questionName = document.getElementById("question-name");
const loaderDiv = document.getElementById("loader");
const timeDiv = document.getElementById("time");
const skipButton = document.getElementById("skip");
const scoreDiv = document.getElementById("score");

const loader = (load = false, fade = false) => {
  if (load) {
    if (fade) {
      loaderDiv.style.display = "";
      loaderDiv.classList.add("animate-fade-in");
      setTimeout(() => {
        loaderDiv.classList.remove("animate-fade-in");
      }, 700);
      return;
    }
    loaderDiv.style.display = "";
  } else {
    loaderDiv.classList.add("animate-fade-out");
    setTimeout(() => {
      loaderDiv.style.display = "none";
      loaderDiv.classList.remove("animate-fade-out");
    }, 700);
  }
};
loader(true);

function loadQuestion(questionIndex) {
  clearInterval(timerInterval);
  startTimer(180);

  const question = quizData[questionIndex];
  questionName.innerText = `Questão ${question.number}`;
  document.title = `Questão ${question.number}`;
  quizContent.innerHTML = "";
  quizAlternatives.innerHTML = "";

  question.content.forEach((content) => {
    if (content.type === "text") {
      const textDiv = document.createElement("p");
      textDiv.innerHTML = content.content;
      quizContent.appendChild(textDiv);
    } else if (content.type === "image") {
      const img = document.createElement("img");
      img.src = content.content;
      img.alt = content.alt;
      img.classList.add("rounded-lg", "w-full", "object-cover", "mb-6");
      quizContent.appendChild(img);
    }
  });

  const alternatives = Object.values(question.alternatives);
  const correctAlternative = alternatives.find(
    (alternative) => alternative.correct
  );
  alternatives.forEach((alternative) => {
    const alternativeLabel = document.createElement("label");
    alternativeLabel.innerHTML = `
            <div id="a-${alternative.alternative_value}" class="select-none border-2 border-gray-200 rounded-xl p-4 cursor-pointer transition duration-300 ease-in-out hover:border-indigo-400 group">
                            <div class="flex items-center">
                                <div class="w-6 h-6 border-2 border-gray-400 rounded-full mr-4 flex items-center justify-center group-hover:border-indigo-500">
                                    <div class="w-3 h-3 bg-indigo-500 rounded-full opacity-0 group-hover:opacity-100 transition-opacity duration-300"></div>
                                </div>
                                <span class="text-lg font-medium text-gray-700 group-hover:text-indigo-700">(${alternative.alternative}) ${alternative.content} </span>
                            </div>
                            <input type="radio" name="answer" class="hidden">
                        </div>`;
    alternativeLabel.classList.add("block", "mb-2");
    const resAnswer = () => {
      checkAnswer(alternative, correctAlternative);
      alternativeLabel.removeEventListener("click", resAnswer);
      quizAlternatives.classList.remove("active");
      quizAlternatives.classList.add("un-active");
    };
    alternativeLabel.addEventListener("click", resAnswer);
    quizAlternatives.appendChild(alternativeLabel);
  });

  quizAlternatives.classList.add("active");
  quizAlternatives.classList.remove("un-active");
  window.scrollTo({ top: 0, behavior: "smooth" });
  setTimeout(() => loader(false, true), 600);
}

function checkAnswer(selected, correct) {
  const isCorrect = selected.correct;
  const selectedDiv = document.getElementById(
    `a-${selected.alternative_value}`
  );
  const correctDiv = document.getElementById(`a-${correct.alternative_value}`);

  if (isCorrect) {
    selectedDiv.classList.add("correct");
    score++;

    setTimeout(() => loadNextQuestion(), 500);
  } else {
    selectedDiv.classList.add("wrong");
    setTimeout(() => loadNextQuestion(), 1500);
  }

  scoreDiv.innerText = `${score} / ${maxScore}`;
  quizData.splice(selected.number - 1, 1);
  correctDiv.classList.add("correct");
}

function startTimer(seconds) {
  let remainingTime = seconds;
  timeDiv.innerText = formatTime(remainingTime);

  timerInterval = setInterval(() => {
    remainingTime--;
    timeDiv.innerText = formatTime(remainingTime);

    if (remainingTime <= 0) {
      clearInterval(timerInterval);
      loadNextQuestion();
    }
  }, 1000);
}

function formatTime(seconds) {
  const minutes = Math.floor(seconds / 60);
  const secs = seconds % 60;
  return `${minutes}:${secs < 10 ? "0" : ""}${secs}`;
}

function loadNextQuestion() {
  currentQuestionIndex = Math.floor(Math.random() * quizData.length);
  loadQuestion(currentQuestionIndex);
}

skipButton.addEventListener("click", loadNextQuestion);

fetch(
  "https://raw.githubusercontent.com/diaslui/enem-extractor/refs/heads/master/examples/output_example/output_prova/output.json"
)
  .then((response) => response.json())
  .then((data) => {
    quizData = data.data;
    maxScore = quizData.length;
    scoreDiv.innerText = `${score} / ${maxScore}`;
    loadQuestion(Math.floor(Math.random() * quizData.length));
  })
  .catch((error) => console.error("JSON Err:", error));
