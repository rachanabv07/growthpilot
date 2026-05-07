import type { WorkflowStep } from "../types/type_job";

interface Props {
  steps?: WorkflowStep[];
}


export default function WorkflowSteps({
  steps
}: Props) {

  return (

    <div className="mt-6">

      <h3 className="font-semibold mb-4">
        Workflow Progress
      </h3>

      <div className="space-y-3">

        {
          steps?.map((step, index) => (

            <div
              key={index}
              className="
                flex
                justify-between
                border
                rounded-lg
                px-4
                py-2
              "
            >

              <span>
                {step.step}
              </span>

              <span className="text-gray-500">
                {step.status}
              </span>

            </div>
          ))
        }

      </div>

    </div>
  );
}
