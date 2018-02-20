import math
from textblob import TextBlob as tb

def tf(word, blob):
    return blob.words.count(word) / len(blob.words)
def n_containing(word, bloblist):
    return sum(1 for blob in bloblist if word in blob.words)
def idf(word,bloblist):
    return math.log(len(bloblist) / (1 + n_containing(word, bloblist)))
def tfidf(word, blob, bloblist):
    return tf(word, blob) * idf(word, bloblist)
document1 = tb("""Players in high school football who are detected with missing or improperly worn equipment during playing action will be removed from the game for at least one down, unless the improper equipment is directly attributable to a foul by the opponent.
This revision in Rule 1-5-5 and other related rules was one of five rules changes for the 2018 season recommended by the National Federation of State High School Associations (NFHS) Football Rules Committee at its January 19-21 meeting in Indianapolis. All changes were subsequently approved by the NFHS Board of Directors.
Rule 1-5-5 also states that if the player is wearing otherwise legal equipment in an illegal manner, the participant must also be replaced for one down. If proper and legal equipment has become improperly worn through use during the game, and prompt repair does not delay the ready-for-play signal for more than 25 seconds, the repair can be made without replacing the player for one down.
In a related change (1-5-4), the head coach is responsible for verifying that all players are legally equipped and will not use illegal equipment. The penalty provisions for any use of illegal equipment remain unchanged and result in an unsportsmanlike foul charged to the head coach.
“I commend the entire football rules committee for its thoroughness and focus on the state of the game of football,” said Todd Tharp, chair of the NFHS Football Rules Committee and assistant director of the Iowa High School Athletic Association. “The committee recognizes that the state of high school football focuses on risk minimization and the responsibility that coaches, players and game officials play in continuing to protect our student-athletes. By emphasizing that the coach is ultimately responsible for assuring his players are using legal equipment by issuing an unsportsmanlike conduct penalty for violations and that players will be removed for using legal equipment in an illegal manner, the committee continues to focus on minimizing risk for all players.”
The second rules change approved by the NFHS Football Rules Committee provides another option for teams in Rule 6-1-9 on fouls committed by the kicking team during free kicks and scrimmage kicks. Now, the receiving team can accept a 5-yard penalty from the succeeding spot. The previous three options remain: accept a 5-yard penalty from the previous spot and have the kicking team re-kick, put the ball in play at the inbounds spot 25 yards beyond the previous spot, or decline the penalty and put the ball in play at the inbounds spot.
Bob Colgate, NFHS director of sports and sports medicine and liaison to the NFHS Football Rules Committee, said this additional option was approved by the committee in an effort to reduce re-kicks, further minimize risks and ensure that appropriate penalties are in place for all fouls.
“The ability to ‘tack on’ penalty yardage on free kicks will potentially reduce the amount of repeated free kicks,” Tharp said. “In addition, this rule change is consistent with NFHS rules that no foul should go unpenalized.”
The third change approved by the committee was a revision related to the examples of a defenseless player. In Rule 2-32-16a, the committee clarified that defenseless player provisions do not apply to a passer until a legal forward pass is thrown. The passer continues to be a defenseless player until the pass ends or the passer moves to participate in the play.
The committee also changed the signal for free-kick infractions, other than encroachment of the neutral zone, from Signal 18 to Signal 19.
The final change approved by the NFHS Football Rules Committee concerned six-player football in Rule 3. The timing rule between periods and intermission for six-player football has been standardized to match the current NFHS rules for 8-player, 9-player and 11-player football.
A complete listing of the football rules changes will be available on the NFHS website at www.nfhs.org. Click on “Activities & Sports” at the top of the home page and select “Football.”
According to the 2016-17 NFHS High School Athletics Participation Survey, football is the most popular sport for boys at the high school level with 1,057,407 participants in 11-player football. Another combined 29,341 boys participated in 6-, 8- and 9-player football. In addition, 2,115 girls participated in one of the four football offerings during the 2016 season.""")
document2 = tb("""NEW ORLEANS, LA. Thursday, February 8, 2018– Continuing a tradition of athletic excellence, St. Augustine High School has named Nathaniel Jones as its new head football coach. Jones served as a defensive coach for the Purple Knight football program and teacher for the past two years. He replaces Al Jones who retired in December after three years as head coach.
“St. Augustine High School is excited about Coach Nathaniel Jones’ new role and salute his contributions to our student-athletes and athletics program,” said Sean J. Goodwin, Principal of St. Augustine High School. “His holistic approach to leadership both in the classroom and on the football field, for the past two years, as well as his coaching experiences have prepared him for this moment.”
During Jones’ two years at St. Augustine, the defensive unit has improved each year. In 2017 Jones coached the Catholic League defensive MVP, Dante’ Carter.
“Coach Jones has a proven track record of building teams focused on success on and off the field,” said Kenneth St. Charles, Ph.D., President and CEO of St. Augustine High School. “We look forward to working with him to build student-athletes with the highest character, emphasizing academics, service, and faith.”
A native of New Orleans, Jones spent two years as an assistant head coach and co-defensive coordinator at the University of St. Francis in Joliet, Illinois, prior to joining St. Augustine. He served as head coach at Edna Karr High School in New Orleans from 2013-2015 leading the program to a 4A state championship runner-up position. In 2013 he was named District 9-4A Coach of the Year. His coaching resume also includes three years as assistant cornerbacks coach at the University of Texas at San Antonio (2011-2013); assistant defensive backs coach at Midwestern State University (2008-2011); one year as assistant cornerbacks coach at Northwestern State University in Natchitoches, LA, Joseph S. Clark High School, and several assistant coaching positions at a variety of high schools.
“Coach Jones emerged as an ideal selection after an exhaustive search which included many excellent applicants. He brings a wealth of coaching and program-building experience and success,” said Barret Rey, St. Augustine Athletic Director.
Coach Nathaniel Jones begins his new role immediately.
“I’m grateful to everyone at St. Augustine for this opportunity. I look forward to building new relationships with alumni, donors, community members and friends of the athletic department that will help strengthen and continue to move the football program to the next level” Jones said. “I am excited and will work diligently to bring the same pride and excellence to Purple Knight football that we know and expect from all aspects of St. Augustine High School.”
Jones graduated from the University of Louisiana at Monroe in 2000 with a Bachelor of Arts degree in General Studies. Jones is married to Jaclyn Jones and they are the proud parents of three daughters Alonah, Faith, and Christian.""")
document3 = tb(""""Although things can't change immediately, I think that because they are taking steps in the right direction, they have heard and are willing to make changes, I think it's becoming a really positive environment and something I want to step back into."
Erceg has only missed four matches while retired, but in that time, the Football Ferns have had a change of coach, with national technical director Andreas Heraf replacing Tony Readings.
Readings resigned in November after six years at the helm, having decided it "probably [was] a good time for someone to come in and put some new thoughts and methods in there," despite having two years to go on his contract.
Erceg said the chance to work under a new coach with new ideas had also played a part in her return.
"With coaches, it's hard for them, because they need to keep their ideas fresh and they need to keep their philosophies fresh. When we were with John Herdman, I think we got caught in the same ideas and the same routines and there was a bit of a drop in performance, and I think the same kind of thing was happening with Tony as well.
"The girls have recognised it and the coach recognised it as well. It's sad that you lose a coach that you've had for so long - obviously he was with us for a good six years - but at the same time you have to be able to adapt and welcome new coaches in.
"I've met with Andreas a couple of times and we've had some really good discussions. I like what he's about, I like his philosophies and I think that he's good for the environment."
Erceg said it has been quite the selfless act for Readings to walk away from the job.
"I could say so many great things about Tony as a person. I don't think anybody's going to say anything bad about him as a person.
"I think it's quite big of him to step back from that role and say there's not a lot more I can get from this, there's not a lot more I can give to the girls, maybe it's time for me to step away. That's a really selfless act, I think.
"He could have quite happily stayed in that role and carried on for the rest of his contract, but he didn't and I think that's a bit of a tribute to the selflessness that he has. He's always put the team first and he's always put the girls first and that's what I've always loved about him.
"It is sad that he's left, but at the same time it is a bit of a business so we have to get the results and we have to get the performances up to scratch, and if we want to perform on the world  stage, I think change there was what we needed."
Gregorius announced her retirement in December 2016,  but has continued playing locally for Upper Hutt City and Capital Football's National Women's League team.
Uncapped midfielder Emma Rolston is the other addition to the squad that played Thailand in November, while there was no room for defender Liz Anton; midfielders Grace Jale, Maggie Jenkins, Elise Mamanu-Gray and Jana Radosavljevic; and forwards Hannah Blake and Aimee Phillips in a smaller travelling party.
Forward Rosie White (foot), midfielder Daisy Cleverley (knee) and winger Paige Satchell (knee) were not considered for selection due to injury.
The pair of friendlies against Scotland take place on March 3 and 6, at Pinatar Football Arena in San Pedro del Pinatar.""")
document4 = tb("""Pederson was grilled for his questionable play-calling in the second half of Kansas City's playoff loss to the Patriots that season. Philly fans didn't have much belief in their new coach. Pederson went through some growing pains as a rookie coach with fans and media questioning his overly aggressive play-calling. Heck, Pederson single-handedly cost the Eagles a win in Dallas that first year with an ill-conceived pass play-call that took his team out of field goal range to ice that game.""")
document5 = tb("""UNM football coach Bob Davie suspended following allegations that his program interfered with assault investigations
The University of New Mexico announced on Thursday they were suspending head football coach Bob Davie for 30 days following two separate investigations involving allegations of misconduct within the athletics department.UNM and Hogan Marren Babbo & Rose, a Chicago law firm hired by the university, investigated the department, specifically alleged physical abuse of football players and "alleged interference with and improper involvement by the football program into police and/or University investigations of sexual and physical assault by football players," according to the report.The firm could not conclude that football coaches or staff obstructed criminal investigations or misconduct cases involving players, per the Albuquerque Journal, but did recommend leadership "take strong action to ensure that the University does not and will not — in any aspect of the University’s program, including athletics — tolerate sexual harassment, sexual assault, physical abuse or other prohibited misconduct against its students."""")
document6 = tb("""National signing day, one of college football’s most exciting events, is rapidly approaching. Tomorrow many of the nation’s most talented high school football players will announce where they plan to play collegiate football and pursue their undergraduate studies.
Many of these young men will hold press conferences in their high school gyms to announce their choice and sign contracts affirming their commitments. Other recruits will opt instead to release professionally produced videos to reveal their college choice. The day will culminate with college administrators, coaches and fans gathering to celebrate the harvest of athletic talent they have reaped. For college football fans, national signing day is a national holiday.
By now, a significant portion of America will have seen Jordan Peele’s Oscar-nominated film Get Out. It is after all, a suitably hip way for viewers to digest the experience of black people in America. Those same people who watched Peele’s film present an unflinching narrative of the ruthless exploitation of black bodies should be mindful of such themes during national signing day. They should consider the optics: young men of superior athleticism, a disproportionate number of whom are black and poor, will be treated like royalty by colleges and universities. But were it not for their athletic talent, they would be invisible to those same institutions.
This first-class treatment of such young men is dispensed because their physical labor secures winning records for collegiate athletic programs, provides million-dollar salaries for their future coaches and supports the billion-dollar industry that benefits athletic departments, college administrators, alumni donors and many other university elites. In many instances, these amateur athletes will do that while being significantly underrepresented in the student body’s overall racial makeup. They will be perceived as athletes on the campus rather than students. It will be, sadly, a university’s ownership of their body that ensures these young men access to the institution, not their intellectual potential.
Research by Shaun Harper, a professor at the University of Southern California, illuminates the harsh reality that black college football players, in particular, have consistently earned college degrees at lower rates than the overwhelming majority of their peers, athletes and nonathletes alike. After retiring, Walter Byers, the founding executive director of the National Collegiate Athletic Association, famously criticized what he called a neo-plantation mentality that exists within many high-level college athletic programs. Such a mentality ultimately maintains a structure where the bulk of the financial gains go to the administrators and coaches, leaving next to nothing for the actual athletes.
In Get Out, Peele offers a brilliant challenge to the use of black bodies -- one that should also be applied to the college sports system. To recap, the film tells the story of Chris, a young black man whose white girlfriend, Rose, plots to have him kidnapped as part of a larger scheme that involves transplanting the brains of elderly white people into young black bodies so that they can experience a vitality that they presume only comes from such bodies. The parallels to college football are unmistakable: it is a system where wealthy and predominantly white coaches are in constant pursuit of young, talented and athletic bodies for their respective programs. Upon attaining that talent, the larger college community will then live vicariously through the toil of those athletes -- the sacrificial lambs of the religion of college football.
In one of the final scenes of the film, Rose, the antagonist, sits eerily in front of her laptop searching the web for future victims using the search phrase “top NCAA prospects.” As a black man and former college athlete, the scene had me uncomfortably shifting in my seat. It served as a vivid reminder of the far too many college athletic programs that resemble “the sunken place,” a place referred to in the film where a victim’s voice is silenced and their consciousness held captive while their bodies are used to benefit others. Former Ohio State University football player Cardale Jones's experience in 2015 highlighted this reality in a very public way. After Jones tweeted a simple question relating to the national conversation about police brutality, he was swiftly told to shut up and focus on winning Ohio State fans another football championship.
Watching the film in a theater, the collective hope of the audience for Chris to escape his plight was palpable. He outstrategized his captors and eventually saved his own life. How can life imitate art within the world of college football so that college football players are more than just bodies for hire?
Perhaps we can start by paying attention to the track record of coaches. While there is no perfect predictor, these three statistics offer suggestions for how a coach has fared as a leader of the field.
Transfer rates. This information is a simple Google search away and a reliable data point for determining the general experience of football players at a given institution. If the program has had a consistent stream of early departures, it may indicate that the promises made in the recruitment process do not match up to the real experience, and it is likely a sunken place.
Graduation rates. This is another reliable predictor of whether bodies are prioritized over minds. It gives insight into how much of a student a football player or other athlete is allowed and encouraged to be.
Course and major clustering rates. A number of football programs make publicly available the academic majors of their football players and student athletes. And it is far too often the case that college athletes are pressured into only pursuing specific classes or academic majors that are perceived as providing the least amount of distraction and resistance to their athletic identity. Recruits will do themselves a favor by scanning the rosters to see how much academic diversity actually exists. Can they pursue a major that they are truly interested in rather than one that will simply keep them eligible? As they look over the roster, if it appears that many of the football players are pursuing the same major, it may, in fact, be a sunken place.
The parallels between Get Out and the college football recruiting process serve as warnings to young black football players in the process of choosing a college or university. They should understand that they are entering into a system where people who look like them will be disproportionately overrepresented on the field and severely underrepresented on the academic sidelines. As it stands, just over 10 percent of college head football coaches are black, while on average 57 percent of college football players are black. Acknowledging this reality -- and that college football has historically created a minefield for black men -- might save them from making the wrong decision, namely missing out on a genuine college education.""")
document7 = tb("""COURT LIES Paisley footy coach accused of abusing young players CLEARED after alleged victim admitted lying to get a bigger compo payout
Retired firefighter John Queen, 63, was arrested and charged with abusing eight youngsters, who can't be named for legal reasons, over a 23-year-period
A PAISLEY football coach accused of abusing young players has been cleared in court after an alleged victim admitted LYING to get a bigger compo payout.
Retired firefighter John Queen, 63, was arrested and charged with abusing eight youngsters, who can’t be named for legal reasons, over a 23-year-period.
Queen has been cleared of abusing young footie players
He always maintained his innocence and had what he described as an unblemished career as a boys club coach.
And he has now been cleared of all wrongdoing after one of his former starlets said he was told to lie to get “extra zeroes” on his victim compensation cheque.
Ex-football coach on trial for ‘abusing Renfrewshire starlet at seaside’
Queen faced 14 charges over his alleged conduct towards youngsters between 1984 and 2007.
Former players claimed he watched them in the showers, dried them, and took them back to his home where he made them shower and then gave them naked massages.
One of the boys, who is now 27, said trainer Queen had earlier plied him with beer before abusing him in their digs aged 15.
The alleged attack happened when the man played with East End Athletic in Renfrewshire.
He said he and his best friend went to police in late 2016 due to media coverage of sex abuse scandals involving celebrities and football coaches.
The ex-starlet also told Kilmarnock Sheriff Court Queen also touched him intimately during a massage.
He said: “I was complaining about growing pains in my legs. He said he’d give them a rub.
“He touched me. I kind of shifted and it stopped.”""")
document8 = tb("""ESU head coach Denny Douds completed his 44th season as head coach at 52nd year on the Warriors' coaching staff overall in 2017. Douds holds the PSAC record for career wins (263) and has coached in 462 career games, a DII record and seventh in NCAA history (all divisions).
Douds will enter the 2018 season as the NCAA's active leader in career wins.
The Warriors had six All-PSAC East selections and three All-Region selections last fall led by redshirt junior tailback Jaymar Anderson, who ran for 1,046 yards and seven touchdowns. Also named All-Region were redshirt junior return specialist Marquis Fells and redshirt freshman fullback Devante Robinson. All three were named to the Football Gazette third team.
Anderson and Fells were named to the All-PSAC East first team, with four on the second team - senior wide receiver Tim Wilson, junior offensive tackle Michael Fleming and senior linebackers Dakota Everett and Sekou Jones.
ESU's student-athletes who signed a National Letter of Intent are listed below.
Rece Bender (WR - 5-10, 170)
Lancaster, Pa./Manheim Township
Coach: Mark Evans
1st team All-Conference defensive back … 2nd team at wide receiver and kick returner … Honor Roll student.
Rich Brown (WR - 6-2, 180)
Philadelphia, Pa./Simon Gratz
Coach: Eric Zipay
1st team All-Philadelphia Public League selection.
Matt DeLaurentis (QB - 6-3, 190)
East Norriton, Pa./Pope John Paul II
Coach: Rory Graver
Offensive MVP of Pioneer Athletic Conference … 1st team All-Conference … Mini Maxwell Award recipient … Honor Roll student.
Carter Forney (WR - 5-11, 180)
Lititz, Pa./Warwick
Coach: Bob Locker
1st team All-Conference wide receiver and defensive back … Honor Roll student.
Zahir Goyins (LB - 6-3, 185)
Voorhees, N.J./Eastern Regional
Coach: John Doherty
Rheyse Green (RB - 5-10, 180)
Scranton, Pa./Scranton
Coach: Mike Marichak
1st team All-Region and honorable mention All-State selection.
Bo Heshler (OL - 6-4, 275)
Harrisburg, Pa./Central Dauphin
Coach: Glen McNamee
1st team All-Conference selection … invited to play in Blue-Grey All-American Bowl.
Anthony Marrone (OL - 6-4, 310)
Lafayette Hill, Pa./Springside Chestnut Hill Academy
Coach: Rick Knox
All-Southeastern PA and All-East Class 3A selection … All-InterAc … rated among top 10 offensive tackles in PA by PA Preps/Rivals … Mr. Pennsylvania Football nominee … selected for U.S. Army All-American Combine and Nike Opening … Honor Roll student.
Nick Nigro (LB - 6-0, 220)
Long Beach, N.Y./Long Beach (Nassau CC)
Coach: Jamel Ramsey
All-Nassau County selection in 2015
Darrin Petrucci (OL - 6-4, 300)
Steelton, Pa./Bishop McDevitt
Coach: Jeff Weachter
1st team All-Keystone Division selection … Honor Roll student.
Nick Sarangoulis (RB - 5-9, 190)
Reading, Pa./Exeter
Coach: Matt Bauer
School's all-time leading rusher … also set single-game rushing record.
Brendan Shaffer (LB - 6-0, 190)
Middletown, Pa./Lower Dauphin
Coach: Greg Kratzer
2-time All-Keystone Conference selection … 1st team running back as a senior and 2nd team as a junior … 1st team defensive athlete and 2nd team linebacker as a junior … Honor Roll student.
Sean Solomon (RB - 5-10, 170)
East Stroudsburg, Pa./East Stroudsburg South
Coach: Ed Christian
Pocono Record Player of the Year … 1st team All-EPC North running back and 2nd team defensive back
Dawson Stuart (QB - 6-4, 210)
Pottstown, Pa./Owen J. Roberts
Coach: Rich Kolka
All-League and All-Area selection … Mini Maxwell Award winner … Honor Roll student.
Davon Thompson (DB - 6-0, 185)
Philadelphia, Pa./Motivation
Coach: Jim Chapman
2-time All-Public League 1st team at safety.
Nick Whitewood (DL - 6-4, 250)
Stroudsburg, Pa./Stroudsburg
Coach: Jim Miller
1st team All-EPC North selection … 2-time All-Conference … All-Area honorable mention.
ESU Football Announces National Letter of Intent Signees
EAST STROUDSBURG - East Stroudsburg University's football program has announced the names of 16 student-athletes who have signed a National Letter of Intent to attend ESU and play football for the Warriors.
Related Headlines
Jimmy Terwilliger Promoted to ESU Football Associate Head Coach
ESU football assistant coach Jimmy Terwilliger has been promoted to associate head coach. Terwilliger, entering his fourth season on ESU's staff, will continue to serve under head coach Denny Douds - the all-time winningest coach in PSAC history and the winningest active coach in NCAA football with 263 career victories entering the 2018 season. 
ESU Football Announces National Letter of Intent Signees
EAST STROUDSBURG - East Stroudsburg University's football program has announced the names of 16 student-athletes who have signed a National Letter of Intent to attend ESU and play football for the Warriors. 
Inge III Named NCAA DII Football Statistical Champion in Forced Fumbles Per Game
EAST STROUDSBURG - East Stroudsburg University redshirt junior free safety Billy Inge III has been named the NCAA Division II football statistical champion for forced fumbles per game during the 2017 season, announced Monday.""")
document9 = tb("""Deuce Prince - OL - 6-2 - 280 - Valhalla, N.Y. - Archbishop Stepinac
Standout offensive lineman at Archbishop Stepinac in Valhalla, N.Y…An All-League selection and Team Captain…Earned Con Ed Athlete of the Week of Westchester County…Recipient of Westchester Football Foundation Golden Dozen Award…Named team's Lineman of the Year…Named to CHSAA Football Golden Eleven Team…Won the New York City and State Football Championship in 2015 & 2017, while finishing as runner-up in 2016…Named Westchester County Top 100 Football Players as a junior…Student Body President in high school…Member of the National Honor Society and Academic All-League and All-County member…Awarded the Joe Riverso Scholarship…Also played high school basketball…Son of Ron and Zoe' Prince…Born August 4, 1999…Nicknamed Deuce because he is Ron Prince II…Father, Ron, played at Appalachian State and is the former Head Coach at Kansas State and has been an NFL Assistant Coach with the Lions, Jaguars, and Colts.""")
document10 = tb("""LOS ANGELES -- What do you see when you look at Sam Darnold and Josh Rosen?
If you're a fan of the New York Giants, San Francisco 49ers or some other basement-dwelling NFL franchise, do you see quarterbacks capable of steering your team out of the darkness?
If you're a casual football fan, do you see two overhyped quarterbacks who have underachieved?
USC's Darnold and UCLA's Rosen entered the season as sure things and have become the ultimate college football quarterback Rorschach test. Perceptions of the two seem to fluctuate weekly, but when their teams meet Saturday (8 p.m. ET on ABC and ESPN App) in what will be their first -- and possibly only -- collegiate encounter, the battle for Los Angeles could very well turn into the battle for the No. 1 pick in the NFL draft.
EDITOR'S PICKS
"They will be running NFL teams shortly," said Washington co-defensive coordinator Jimmy Lake.
That's the consensus among a number of coaches familiar with Darnold and Rosen.
In college football, there's a tendency to obsess over stats without fully comprehending the exact story behind them. Darnold and Rosen have been meticulously -- and sometimes mercilessly -- analyzed this season, but those who follow them most closely in the college game don't bat an eye after watching them play.
"Hopefully they both decide to enter the draft and move on to the next level after this year," said Stanford defensive coordinator Lance Anderson, who faced both quarterbacks this season.
If both decide to leave college early and enter the NFL draft, they will undoubtedly be two of the first players selected. There's little question about their talent, but they've been polarizing figures in the quarterbacking world because of their on-field inconsistencies. Darnold has No. 11 USC (9-2) in the Pac-12 championship game but on the outside of the College Football Playoff. Rosen is trying to lead UCLA (5-5) to a bowl berth.
So how do coaches and scouts look past the stats when evaluating Darnold and Rosen? It's easy: They really look at the film and each quarterback's supporting cast.
Last season, Darnold came off the bench to throw for 3,086 yards with 31 touchdowns and nine interceptions. He went 9-1 as a starter and guided the Trojans to a 52-49 Rose Bowl win over Penn State. He entered this season as the Heisman Trophy favorite. Yet, last week's win over Colorado was his first game this season without turning the ball over.
Darnold has admitted to forcing passes and not taking what defenses have given him at times. But as coaches around the country have pointed out, a banged-up offensive line and a dearth of NFL-caliber receiving talent has burdened Darnold, who also dealt with a sprained ankle for more than a month this season.
"It doesn't matter if Tom Brady is the quarterback for Oregon State, if he doesn't have a line that can block and he doesn't have guys to throw to, then you're going to have certain things to do [as a defensive coordinator] to game plan, even though he's ultra-talented," said a Pac-12 defensive coordinator, who has faced both Darnold and Rosen over the last two seasons.
"A quarterback can't do it all himself, and maybe right now [they're] trying to do it all."
USC offensive coordinator Tee Martin met a question about Darnold's perceived struggles with a smile that hinted at annoyance. For starters, he liked his young quarterback (Darnold is a redshirt sophomore) forcing what he thought were NFL throws to unseasoned receivers because it showed the trust he had in his young teammates. It was a way to build chemistry and put more responsibility on a group that Darnold was bringing along on the fly.
It's also showing how much Darnold trusts his arm. To Martin, who was a national-championship-winning quarterback at Tennessee in 1998, he has a quarterback who is making NFL throws to college players.
Sam Darnold has passed for 3,198 yards with 24 touchdowns and 11 interceptions. Matthew Stockman/Getty Images
"Three or four [forced passes], I can live with because you're competing and you want to give a guy a chance to make a play and it's 50-50," Martin said. "Some of them have gone our way, some of them haven't gone our way, but I don't want to take that from him."
As one Pac-12 defensive coordinator told ESPN, even Darnold's inconsistencies didn't deter an NFL scout from telling him that he'd be shocked if Darnold wasn't the first pick in next year's draft. "Every time I see him play, I see a really good player," the coordinator said. "That [scout] kind of confirmed it."
UCLA coach Jim Mora agreed with Martin's assessment and he believes the same can be said for Rosen. He sees elite players looking to make elite plays that aren't always there. Mora, who has an extensive NFL background, sees two early-round draft picks who are processing things like NFL quarterbacks would.
"They're both very intelligent and they see the game the way a quarterback is supposed to see the game," Mora said. "I can tell you this: I will always take a young man that is aggressive and has that type of attitude over somebody who doesn't. You can teach them to improve their decision-making, but I don't know that you can always teach competitiveness and I love [Rosen's] competitiveness."
During the month of September, Rosen led the nation with 427 passing yards per game and 17 touchdowns to just five interceptions. In a season-opening win over Texas A&M, he helped the Bruins erase a 34-point, third-quarter deficit with 292 yards and four touchdowns in the fourth quarter.
However, his numbers have dipped. He's thrown four touchdowns to four interceptions in his last three-and-a-half games. He suffered a concussion and was taken out in the third quarter of the Washington game on Oct. 28 and missed the following game against Utah. Rosen has had to work with a depleted offense -- injuries have mounted at receiver and his top two tight ends went down -- and keep up with a defense surrendering a 38.6 points per game.
Washington State defensive coordinator Alex Grinch said his plan against Darnold was to constantly jam receivers at the line to slow down routes, giving his front seven more time to gash USC's banged-up offensive line. The Cougars held Darnold to a career-low 164 yards as a starter with an interception and a game-sealing fumble in a 30-27 win, but Grinch said he never assumed Darnold would grow careless.
"He has that innate ability to find that receiver that's breaking open at that exact time that he does," said Grinch. "He has a real command when you look at him."
As for Rosen, Lake is impressed by how effortlessly he delivered passes and how frequently he made the toughest passes look easy. He also thinks that Rosen gets the ball out faster than Darnold.
"He has all the arm talent you could you could think of -- he makes every single throw," Lake said. "I am 100 percent positive any coach in the National Football League will think once they get their hands on him, they'll be able to mold him into whatever type of quarterback they like to have for their system. He'll be for sure one of the best quarterbacks we face, if not the best quarterback we face this year.
"If he sees a throw that's supposed to be covered, he's going to throw it anyway because he believes in his arm talent, as he should."
Where Darnold holds a big edge over Rosen is movement outside of the pocket.
"He's definitely more athletic than I am," Rosen said.
Don't let his 6-foot-4, 220-pound frame fool you: Darnold has wheels and wiggle. He isn't Reggie Bush, but he certainly isn't Jared Lorenzen.
Darnold has a QBR of 68.2 on passes outside the pocket, completing 55.8 percent of his passes with a nation-leading six touchdowns with two interceptions. He's also averaging 7.8 yards per attempt and has a nation-best 603 yards, 11 completions of 20-plus yards and 27 first downs. Darnold has 169 scramble yards and ranks sixth nationally with nine scrambles of 10-plus yards.
"You just see how he bobs and weaves in the pocket," said Lake. "If the throw's not there, he can easily scramble and get first downs."
Darnold said that he thinks he's been dangerous on the move because of playing different sports and different positions in football through his high school years. He isn't afraid to take off running and or get physical in order to grind out an extra yard or two.
"If you went into an alley to get into a fistfight, you want Sam with you," said a Power 5 assistant who recruited Darnold and Rosen in high school. "If you went into a math or a chess match, you want Josh with you."
Rosen isn't a statue, but he's not comfortable outside the pocket, where he has a QBR of 7.8, is completing 35.3 percent of his passes, averages 3.2 yards per attempt and has thrown three touchdowns to one interception.
However, both Darnold and Mora complimented Rosen's in-pocket movement. Mora said he is impressed by Rosen's ability to feel pressure in the pocket and step up and back. Darnold called Rosen's pocket anticipation "top-notch."
"I like to call it sneaky athleticism because when he's back there he's kind of just moving pretty methodically and then when he needs to move it's really violent," Darnold said.
A Power 5 assistant who recruited both quarterbacks said the thing that originally drew him to Rosen was how quickly his off-field intelligence translated to the playing field. It was almost as if Rosen was playing a game within a game with opposing coaches and what they drew up.
"He has the confidence that most defensive coordinators don't like because he'll challenge a defensive coordinator and he's overly confident with it," the assistant said. "It kind of hurts him sometimes and sometimes it makes him look like a genius.
"He's phenomenal, though. I've never been around a quarterback so talented in my entire life. Josh has eyes in the back of his head, I swear."
When it comes to pure passing ability, most coaches who spoke to ESPN gave Rosen the advantage. When it came to the intangibles, especially mobility, Darnold won out. As far as who should be drafted first, coaches were split, which might add another layer to Saturday's game.
They'll be observed intently for how they play in what is arguably the best matchup of pure quarterback talent college football has to offer.
"It's awesome and it's a really, really cool storyline to be linked with Josh, being in the same class come out of high school and all that stuff," Darnold said. "When it comes down to it, it's just two quarterbacks competing ... and we just happen to be really good players."""")
bloblist = [document1,document2,document3,document4,document5,document6,document7,document8,document9,document10]
for i, blob in enumerate(bloblist):
    print("Top words in document {}".format(i+1))
    scores = {word: tfidf(word, blob, bloblist) for word in blob.words}
    sorted_words = sorted(scores.items(), key=lambda x: x[i], reverse=True)
    for word, score in sorted_words[:10]:
        print("\tWord: {}, TF-IDF: {}".format(word, round(score, 5)))
#document 1 = 7ad8245bde3bdad2ae63d44320e0dcbe2165c61a.html
#document 2 = 7d104b22269f8be52ec46c98ddea08dd28673510.html
#document 3 = 2634e5daa477bd8bf53efdf8be56a8d22b54eb27.html
#document 4 = d326d33cd6a6eb21a3c896072c96926c61c6ae8d.html
#document 5 = b242ca0eaecc2a21a91e5ab5dc7500ce6e88abde.html
#document 6 = b8422d2e1522fe400fe5d584b8569a95faea3a8f.html
#document 7 = 9a2da78a6c9ee32122f8627bb404553764a5f793.html
#document 8 = 099ba93e9fb5f3a157b91ffd2fcc2e2508d62c6d.html
#document 9 = 35bd55bb59dd86aa36b26603fd02a4d654c4cf3b.html
#document 10 = 8d771667a4c46ebad6811dd69560542390d81b21.html
