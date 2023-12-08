from PIL import Image
import streamlit as st

st.set_page_config(page_title='Multipage App', page_icon='🤖', layout='wide')


img_contact_form= Image.open('images/maxresdefault.jpg')
silop_cave= Image.open('images/silop_cave.jpg')
mabua_beach= Image.open('images/mabua_beach.jpg')
floatingvil= Image.open('images/Floatingvil.jpg')
sagisiisland= Image.open('images/sagisi.jfif')
Buenavista= Image.open('images/buenavistacave.jpg')
lakemainit= Image.open('images/Lake-Mainit.jpg')
alingkakajaw= Image.open('images/alingkakajaw.jpg')
battleofsurigao= Image.open('images/battle_of_surigao.jpg')
balingangafalls= Image.open('images/balinganga.jpeg')
songkoycoldspring= Image.open('images/songkoy-cold-spring.jpg')

with st.container():
    left, center, right = st.columns((1.5, 2, 1.5))
    with center:
        st.title('Things to do in Surigao City')


with st.container():
    column, column2, colum = st.columns((0.01, 2, 0.01))
    with column2:
      st.write('###')
      st.image(img_contact_form)
    with colum:
        st.empty()
    with column:
        st.empty()

with st.container():
    st.write('---')
    st.title('Introduction')
    st.write("""
    
Welcome to Surigao City, a captivating destination nestled in the heart of the Philippines, where natural wonders meet 
cultural treasures. This vibrant city, located in the province of Surigao del Norte, invites travelers to embark on a 
journey filled with diverse experiences. From breathtaking landscapes to rich historical heritage, Surigao City offers a 
tapestry of activities for every type of explorer.

Nature enthusiasts can revel in the awe-inspiring beauty of the famed Enchanted River, where crystal-clear waters weave 
through lush surroundings, creating a magical setting. Explore the captivating landscapes of Tinuy-an Falls and witness 
the majesty of a multi-tiered waterfall, providing a serene escape into nature's embrace.

For those seeking adventure, the renowned Cloud 9 surf spot awaits, promising exhilarating waves for surfing enthusiasts. 
Dive into the underwater wonders of Siargao, a nearby island, renowned for its vibrant coral reefs and diverse marine 
life.

Delve into the city's rich history by visiting the Surigao Provincial Museum, where artifacts and exhibits narrate the 
tale of the region's cultural evolution. Stroll through the charming streets and visit the iconic Surigao Cathedral, a 
testament to the city's deep-rooted religious heritage.

Surigao City is not just a destination; it's an invitation to explore, discover, and immerse yourself in the beauty and 
culture that define this enchanting corner of the Philippines. Whether you seek tranquility in nature, the thrill of 
adventure, or a glimpse into the past, Surigao City welcomes you with open arms and promises an unforgettable journey.

    """)
st.subheader('So here are the places you can go and have some fun adventures...')

with st.container():
    st.write('---')
    st.header('1.  Silop Multi-Caves')
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(silop_cave)
    with text_column:
        st.subheader('Silop Multi_Caves')
        st.write(
            """One of Suirgao City's tourist attraction, Silop Cave is a multi cave system located just few minutes
            away from the city proper. It is composed of six cave systems of which the two are open for tourist 
            exploration.
            """
        )
        st.markdown('[Learn more...](https://www.tripadvisor.com.ph/Attraction_Review-g1459886-d2043745-Reviews-Silop_Multi_Caves-Surigao_City_Surigao_del_Norte_Province_Mindanao.html)')

with st.container():
    st.write('##')
    st.header('2.  Mabua Pebble Beach')
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(mabua_beach)
    with text_column:
        st.subheader('Mabua Pebble Beach')
        st.write(
            """Mabua Pebble Beach, located 30 minutes from the city center of Surigao, 
            stands out among Filipino beaches due to its unique shoreline composed of smooth white pebbles. 
            Unlike most beaches formed by wind and wave movements, Mabua Pebble Beach likely resulted from strong 
            forward swashing waves pushing pebbles onshore and weaker return swashing waves depositing the material. 
            The varied sizes and shapes of the pebbles, mainly oval, have a dual purpose—aside from their aesthetic 
            appeal, walking barefoot on them is considered therapeutic by reflexologists due to the feet's reflex points 
            connected to internal organs.
        """
        )
        st.markdown('[Learn more...](https://guidetothephilippines.ph/destinations-and-attractions/mabua-pebble-beach)')

with st.container():
    st.write('##')
    st.header('3.  Day-Asan Floating Villages')
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(floatingvil)
    with text_column:
        st.subheader ('Day-Asan Floating Villages')
        st.write(
            """No words can probably describe the beauty and silent charm of Day-asan Floating Village in Surigao City. 
            Hailed as the “Little Venice of Surigao City”, the village is a fishing village consisting of houses on 
            wooden stilts above the water. It is a barangay in Surigao City, the capital of the province of Surigao del 
            Norte in the Caraga Region of Mindanao.
            """
        )
        st.markdown('[Learn more...](https://www.vigattintourism.com/tourism/articles/Day-asan-Floating-Village-Little-Venice-of-Surigao-City)')

with st.container():
    st.write('##')
    st.header('4.  Sagisi Island')
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(sagisiisland)
    with text_column:
        st.subheader ('Sagisi Island')
        st.write(
            """Is a tropical island paradise of white sand beach, deep blue sea waters and shades from lofty coconut 
            trees, Sagisi offers the perfect hideaway to enjoy the sun, the sand and the sea. The island's coral reef 
            teeming with lushly preserved marine life also provides enthusiasts with one of the most excellent diving 
            sites ever known in the Philippines.  Sagisi is accessible by a one-hour pumpboat boat ride from the city 
            proper.
            """
        )
        st.markdown('[Learn more...](https://www.vigattintourism.com/tourism/articles/Surigao-The-City-of-Island-Adventures)')

with st.container():
    st.write('##')
    st.header('5.  Buenavista Cave')
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(Buenavista)
    with text_column:
        st.subheader ('Buenavista Cave')
        st.write(
            """Buenavista Cave is primarly a dripstone cave. The wealth of formations is named King's Court, as it 
            resembles a huge group of persons. Some 100 meters from the main entrance is an underground pool which is 
            knee deep. The cave has three different entrances. Buenavista Cave is located at Barangay Buenavista on 
            Hikdop Island and is reached from the capital in 45 minutes by pumpboat.
        """
                 )
        st.markdown('[Learn more...](https://www.traveltothephilippines.info/2020/07/05/buenavista-cave-amazing-stone-formation/)')

with st.container():
    st.write('##')
    st.header('6.  Lake Mainit')
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(lakemainit)
    with text_column:
        st.subheader ('Lake Mainit')
        st.write(
            """Lake Mainit, lake on the border of Surigao del Norte and Agusan del Sur provinces, northeastern Mindanao,
             Philippines. It is the country’s fourth largest lake and has an area of 58 sq mi (150 sq km). Its outlet is 
             the Tubay River, which flows southward before entering Butuan Bay of the Mindanao Sea. Lake Mainit is skirted 
             on the east by the Philippine–Japan Friendship Highway, connecting Surigao and Davao. The area has secondary
              forests, and rice, corn (maize), and bananas are grown.
            """
        )
        st.markdown('[Learn more...](https://lmda.wordpress.com/about-lake-mainit/)')

with st.container():
    st.write('##')
    st.header('7.  Alingkakajaw Islands')
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(alingkakajaw)
    with text_column:
        st.subheader ('Alingkakajaw Islands')
        st.write(
            """Alingkakajaw Island was a symbol of fighting little paradise behind the huge mining activities but still 
            lots of attraction from the incoming visitors whether international or local because of its presence in the 
            sea, perfectly untouched and unexploited little paradise. Those bypassing visitors when crossing the port of 
            Hayanggabon en route to Bucas Grande Islands will ever make a turn to look into something beautiful and 
            endearing that will make their day alive and thinking about something pleasant that is going to happen.
            """
        )
        st.markdown('[Learn more...](https://www.expedia.com.ph/Alingkakajaw-Island-Surigao.d553248621562598253.Place-To-Visit)')

with st.container():
    st.write('##')
    st.header('8.  Batlle of Suirgao Strait Museum')
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(battleofsurigao)
    with text_column:
        st.subheader ('Batlle of Suirgao Strait Museum')
        st.write(
            """Surigao City — The Battle of Surigao Strait (BOSS) Memorial and Museum officially opened to the public 
            here with the presence of dignitaries and ships from the Royal Australian Navy (RAN), the Philippine Navy 
            (PN) and the Philippine Coast Guard (PSG).
            """
        )
        st.markdown('[Learn more...](https://mindanaogoldstardaily.com/archives/104068)')

with st.container():
    st.write('##')
    st.header('9.  Balinganga Falls')
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(balingangafalls)
    with text_column:
        st.subheader ('Balinganga Falls')
        st.write(
            """Surigao del Sur is one of the provinces in the Philippines which is famous for its mysterious yet amazing tourist spots.

You might have heard some of the famous tourist spots in Surigao del Sur like the magical river or the breath-taking 
waterfalls. Indeed, Surigao del Sur is a blessed with beautiful destinations. Facing the Pacific Ocean, its stunning 
islands are inviting for some island-hopping activities.
            """
        )
        st.markdown('[Learn more...](https://touristspotsfinder.com/surigao-del-sur-tourist-spots/)')

with st.container():
    st.write('##')
    st.header('10.  Songkoy Cold Spring')
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(songkoycoldspring)
    with text_column:
        st.subheader ('Songkoy Cold Spring')
        st.write(
            """Surigao del Sur is one of the provinces in the Philippines which is famous for its mysterious yet amazing tourist spots.
You might have heard some of the famous tourist spots in Surigao del Sur like the magical river or the breath-taking 
waterfalls. Indeed, Surigao del Sur is a blessed with beautiful destinations. Facing the Pacific Ocean, its stunning 
islands are inviting for some island-hopping activities.
            """
        )
        st.markdown('[Learn more...](https://touristspotsfinder.com/surigao-del-sur-tourist-spots/)')

with st.container():
    st.write('###')
    st.write('---')
    st.header('Conclusion')
    st.write("""
Surigao, located in the Philippines, offers a diverse range of activities for visitors seeking both natural beauty and 
cultural experiences. In conclusion, a trip to Surigao promises a captivating blend of stunning landscapes, vibrant 
marine life, and rich cultural heritage. From exploring the enchanting Sohoton Cove and captivating Bucas Grande Islands 
to engaging in water activities like surfing in Cloud 9, Surigao caters to both adventure enthusiasts and those seeking 
a more relaxed getaway. Immerse yourself in the local culture by visiting the historic Mabua Pebble Beach and 
experiencing the warmth of the Surigaonon people. The province('s unique combination of pristine beaches, lush forests, 
and cultural richness makes Surigao an ideal destination for travelers looking for an unforgettable and well-rounded 
experience.
    """)

with st.container():
    st.write('###')
    st.write('###')
    st.write('If you want more information please [Contact](http://localhost:8501/contact) as...')