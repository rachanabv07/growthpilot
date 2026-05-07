const API_URL = "https://growthpilot-1.onrender.com";


export async function fetchJobs() {

  const response = await fetch(
    `${API_URL}/jobs`
  );

  return response.json();
}
