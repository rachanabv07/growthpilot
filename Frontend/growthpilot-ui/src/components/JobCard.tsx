import type { Job } from "../types/type_job";

import StatusBadge from "./StatusBadge";

import WorkflowSteps from "./WorkflowSteps";


interface Props {
  job: Job;
}


export default function JobCard({
  job
}: Props) {

  return (

    <div
      className="
        bg-white
        rounded-2xl
        border
        shadow-sm
        p-6
      "
    >

      {/* HEADER */}

      <div className="flex justify-between items-start">

        <div>

          <h2 className="text-2xl font-bold">

            {job.input_data.event}

          </h2>

          <p className="text-gray-500 mt-2">

            {job.input_data.note}

          </p>

          <p className="text-sm text-gray-400 mt-1">

            {job.input_data.date}

          </p>

        </div>

        <StatusBadge status={job.status} />

      </div>


      {/* WORKFLOW STEPS */}

      <WorkflowSteps steps={job.steps} />


      {/* GENERATED CONTENT */}

      {
        job.result?.content && (

          <div className="mt-8">

            <h3 className="text-xl font-semibold mb-4">

              Generated Content

            </h3>

            <div className="space-y-5">


              {/* HOOK */}

              <div>

                <p className="text-sm font-medium text-gray-500">

                  Hook

                </p>

                <p className="mt-1 text-lg font-medium">

                  {job.result.content.hook}

                </p>

              </div>


              {/* BODY */}

              <div>

                <p className="text-sm font-medium text-gray-500">

                  Body

                </p>

                <p className="mt-1 text-gray-700 whitespace-pre-line">

                  {job.result.content.body}

                </p>

              </div>


              {/* CTA */}

              <div>

                <p className="text-sm font-medium text-gray-500">

                  CTA

                </p>

                <p className="mt-1 font-medium">

                  {job.result.content.cta}

                </p>

              </div>


              {/* HASHTAGS */}

              <div>

                <p className="text-sm font-medium text-gray-500 mb-2">

                  Hashtags

                </p>

                <div className="flex flex-wrap gap-2">

                  {
                    job.result.content.hashtags?.map(
                      (tag: string, index: number) => (

                        <span
                          key={index}
                          className="
                            bg-gray-100
                            text-gray-700
                            px-3
                            py-1
                            rounded-full
                            text-sm
                          "
                        >
                          {tag}
                        </span>
                      )
                    )
                  }

                </div>

              </div>

            </div>

          </div>
        )
      }


      {/* EVALUATION */}

      {
        job.result?.evaluation && (

          <div
            className="
              mt-8
              border
              rounded-xl
              p-4
              bg-gray-50
            "
          >

            <h3 className="font-semibold mb-3">

              Evaluation

            </h3>

            <div className="space-y-2">

              <p>

                <span className="font-medium">
                  Score:
                </span>

                {" "}

                {job.result.evaluation.score}

              </p>

              <p>

                <span className="font-medium">
                  Approved:
                </span>

                {" "}

                {
                  job.result.evaluation.approved
                    ? "✅ Yes"
                    : "❌ No"
                }

              </p>

            </div>

          </div>
        )
      }


      {/* GENERATED IMAGE */}

      {
        job.result?.image?.url && (

          <div className="mt-8">

            <h3 className="text-xl font-semibold mb-4">

              Generated Creative

            </h3>

            <img
              src={job.result.image.url}
              alt="generated creative"
              className="
                rounded-2xl
                border
                shadow-sm
                w-full
              "
            />

            {
              job.result?.image?.prompt && (

                <div
                  className="
                    mt-4
                    bg-gray-50
                    border
                    rounded-xl
                    p-4
                  "
                >

                  <p className="text-sm font-medium text-gray-500">

                    Image Prompt

                  </p>

                  <p className="mt-2 text-sm text-gray-700 whitespace-pre-line">

                    {job.result.image.prompt}

                  </p>

                </div>
              )
            }

          </div>
        )
      }


      {/* ERROR STATE */}

      {
        job.status === "failed" && (

          <div
            className="
              mt-8
              bg-red-50
              border
              border-red-200
              rounded-xl
              p-4
            "
          >

            <p className="text-red-700 font-medium">

              Workflow Failed

            </p>

            <p className="text-red-500 mt-2 text-sm">

              {
                job.result?.error
              }

            </p>

          </div>
        )
      }

    </div>
  );
}