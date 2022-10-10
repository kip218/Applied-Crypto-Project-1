#include<iostream>
#include<string>
#include<vector>

void charCount (std::string msg){
    int sp_count = 0;
    int alpha_count = 0;
    std::vector<int> vec;
    for (int i = 0; i < msg.length(); i++){
        if (isspace(msg[i])){
            sp_count++;
            vec.push_back(alpha_count);
            alpha_count = 0;
        }
        else{
            alpha_count++;
        }
    }
    std::cout << std::endl;
    std::cout << "There are " << sp_count << " space char.\n";
    std::cout << "vec char:\n";
    for (int x : vec)
        std::cout << x << ' ';
    std::cout << std::endl;
}

int main(){
    std::string msg1 = "autarchy muggiest capabilities snowier collect undivided superpower aspca tektites neuritis turtledoves miriest nonsectarian featherbrained confiscators glimpse domesticator dater houston bassoon antipathy lowdown hallucinative noses drowse wordlessly remembering lessening escargot intersects horace unroofs smokable wirepuller exteriorized auctioned cavils uprose sobbing preannouncements pests noodled minter symbiot rocketlike oops unalike readableness vivo affirmativeness plumier spaciously miseducating recessionals herbaceous recipient evanesce tightrope rester deleteriousness undiscriminati";
    std::string msg2 = "wanning objectively bicyclers footmark unbutton clockworks yanks distinctively miosis headed reinduction enchanters colleges smirkiest disobliges pageant nubbier victualler beastly teazling indigens demon parser treasurable phrenological flaxseeds interdepartmental filibustered selvedges trode helplessly woefuller ridder redigesting runtish swirling naught corselet pathogeny excommunicates lappets hug basing disassociating rajah pontificator shenanigans glowworm eels halfbacks bonder psychoanalysts methamphetamine rabidly eleven fabulously apprizer lifeway peccadilloes saltatory cetera damnit";
    std::string msg3 = "mettle bribe dignified topsoil groundmass sorrowfully mondays veneris provender surveyance metallurgy bowl telecasting blandest admonisher desexualization putters admen snaillike tableaux around candlewick oncogenic splintered comp anxiously overdrives misalignments condemns bars referenced sixty contritely astrally dehumidify voile frumenties vile trifles pronghorns huskies marketeers entirely spence incarnations straiten ate abetter blower decreer kayoes ungraciously quarry buttoners bumbles banjos gabbing reoccupation tanbarks brushier tycoons sixtieth motioning unsymmetrically woald stippl";
    std::string msg4 = "charlatans aphoristically commixt oxidise vigilante antisocial blip reinserting slicer crescent fructuary sanctioning quintains configurative yogin overbuying xylan likeness amicability yammered medicates succeeder knackeries keepings finagle ghoulish cretaceous shellers fellable dedicatee microanalytical coalitions hijackers preallotting representatives capitally fosters passives individualizes affrayers tactlessly throes reintrenched fivefold pensioned seville expectorator outleap impedance proconsul suburb valiancy crowbars basso gibbeting documents errant positive dustman alveoli stylebook";
    std::string msg5 = "smile splintered propitiously sudser looter tunnies bummers kinematical jubilant shushes railings suffrage precedence sheepskins insularity regainer tallowed jaggedly legacy requiting stumblers chiaroscuros dislodged raining biceps skirtings detacher anthropoidea reliquary suits shovelhead billet saturable guiding transvestites scowler preparatory pencils vomit encouraged mustering reincarnate steers burrowers eeliest compulsion jeopardies abstractionists time jugular sagacity intangibles vitalist noncombatants mesentery legends ham larruped bummer aryan abstract weatherbound chrisms qursh qui";
    std::vector<std::string> all_msg{msg1, msg2, msg3, msg4, msg5};
    for (int i = 0; i < all_msg.size(); i++){
        
        charCount(all_msg[i]);
        std::cout<< "Total chars: " << all_msg[i].length() << std::endl;
    }
    return 0;
}