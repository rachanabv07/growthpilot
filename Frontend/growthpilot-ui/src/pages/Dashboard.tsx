import { useEffect, useState } from "react";

import Navbar from "../components/Navbar";

import JobCard from "../components/JobCard";

import { fetchJobs } from "../api/jobs";

import type { Job } from "../types/type_job";


export default function Dashboard() {

  const [jobs, setJobs] = useState<Job[]>([]);

  async function loadJobs() {

    try {

      const data = await fetchJobs();

      setJobs(data);

    } catch (error) {

      console.error(error);
    }
  }

  useEffect(() => {

    loadJobs();

    const interval = setInterval(
      loadJobs,
      3000
    );

    return () => clearInterval(interval);

  }, []);

  return (

    <div className="min-h-screen bg-gray-50">

      <Navbar />

      <main className="max-w-6xl mx-auto p-8">

        <div className="mb-10">

          <h1 className="text-4xl font-bold">

            AI Campaign Dashboard

          </h1>

          <p className="text-gray-500 mt-2">

            Autonomous AI-generated
            LinkedIn campaigns

          </p>

        </div>

        <div className="space-y-8">

          {
            jobs.map((job) => (

              <JobCard
                key={job.id}
                job={job}
              />
            ))
          }

        </div>

      </main>

    </div>
  );
}
