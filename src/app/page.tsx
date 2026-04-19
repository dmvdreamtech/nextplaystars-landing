import Nav from "@/components/ui/Nav";
import Footer from "@/components/ui/Footer";
import Hero from "@/components/sections/Hero";
import RecruitingReality from "@/components/sections/RecruitingReality";
import MeetNikki from "@/components/sections/MeetNikki";

export default function Home() {
  return (
    <>
      <Nav />
      <main>
        <Hero />
        <RecruitingReality />
        {/* Section 3: How NextPlay Works — next */}
        <MeetNikki />
        {/* Section 5: Built by a coach */}
        {/* Section 6: Pricing */}
        {/* Section 7: Final CTA */}
      </main>
      <Footer />
    </>
  );
}
