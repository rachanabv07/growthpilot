interface Props {
  status: string;
}


export default function StatusBadge({
  status
}: Props) {

  const styles: Record<string, string> = {

    pending:
      "bg-yellow-100 text-yellow-700",

    running:
      "bg-blue-100 text-blue-700",

    completed:
      "bg-green-100 text-green-700",

    failed:
      "bg-red-100 text-red-700",
  };

  return (

    <span
      className={`
        px-3 py-1 rounded-full text-sm font-medium
        ${styles[status]}
      `}
    >
      {status}
    </span>
  );
}