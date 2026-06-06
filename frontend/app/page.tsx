export default function Home() {
  return (
    <main className="min-h-screen">
      <section className="h-screen bg-cover bg-center flex items-center justify-center"
        style={{ backgroundImage: "url('/hero.jpg')" }}>
        <div className="bg-black/40 p-8 rounded">
          <h1 className="text-4xl md:text-6xl font-bold">Jet Ski Taormina</h1>
          <p className="mt-4 max-w-xl">Premium, guided excursions around Isola Bella.</p>
          <div className="mt-6 flex gap-4">
            <a href="/book" className="px-6 py-3 bg-white text-black rounded">Book Now</a>
            <a href="/gallery" className="px-6 py-3 border border-white rounded">View Experiences</a>
          </div>
        </div>
      </section>
    </main>
  );
}
