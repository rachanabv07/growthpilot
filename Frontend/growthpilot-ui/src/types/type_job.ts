export interface Job {

  id: string;

  status: string;

  steps?: WorkflowStep[];

  input_data: {
    event: string;
    note: string;
    date: string;
  };

  result?: {
    content?: {
      hook: string;
      body: string;
      cta: string;
      hashtags: string[];
    };

    evaluation?: {
      score: number;
      approved: boolean;
    };

    image?: {
      url: string;
      prompt: string;
    };

    error?: string;
  };
}

export interface WorkflowStep {
  step: string;
  status: string;
}
