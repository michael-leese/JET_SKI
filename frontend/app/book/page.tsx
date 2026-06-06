"use client";
import { useState } from "react";
export default function BookPage() {
  const [form, setForm] = useState({ name: "", email: "", experience_id: 1, start_time: "" });
  const submit = async (e: React.FormEvent) => {
    e.preventDefault();
    await fetch(`${process.env.NEXT_PUBLIC_API_URL || "http://localhost:8000"}/api/bookings/create`, {
      method: "POST", headers: { "Content-Type": "application/json" }, body: JSON.stringify(form)
    });
    alert("Booking created (pending). Payments coming next.");
  };
  return (
    <main className="p-6 max-w-xl mx-auto">
      <h1 className="text-3xl font-semibold">Book an Experience</h1>
      <form className="mt-6 grid gap-4" onSubmit={submit}>
        <input className="p-3 bg-gray-900 border border-gray-700 rounded" placeholder="Name"
          value={form.name} onChange={e => setForm({ ...form, name: e.target.value })}/>
        <input className="p-3 bg-gray-900 border border-gray-700 rounded" placeholder="Email"
          value={form.email} onChange={e => setForm({ ...form, email: e.target.value })}/>
        <input className="p-3 bg-gray-900 border border-gray-700 rounded" placeholder="Start time (ISO)"
          value={form.start_time} onChange={e => setForm({ ...form, start_time: e.target.value })}/>
        <button className="px-6 py-3 bg-white text-black rounded" type="submit">Confirm</button>
      </form>
    </main>
  );
}

