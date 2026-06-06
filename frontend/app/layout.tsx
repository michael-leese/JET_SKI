export const metadata = {
  title: "Taormina Jet Ski & Excursions",
  description: "Premium jet ski experiences in Taormina and Isola Bella.",
  openGraph: { title: "Taormina Jet Ski", type: "website" },
};
export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (<html lang="en"><body className="bg-black text-white">{children}</body></html>);
}
