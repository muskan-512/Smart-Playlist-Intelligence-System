n = int(input("Enter the size of the list: "))
Playlist = [0] * n

for i in range(n):
    Playlist[i] = int(input("Enter the duration of songs in seconds(s): "))

print("Playlist:", Playlist)

invalid = False
for duration in Playlist:
    if duration <= 0:
        invalid = True
        break

if invalid == True:
    print("Invalid Playlist")
else:
    Total_duration = sum(Playlist)
    Number_of_songs = len(Playlist)
    repetitive = False
    for duration in Playlist:
        if Playlist.count(duration) > 1:
            repetitive = True
            break
    if Total_duration < 300:
        category = "Too Short Playlist"
        recommendation = "Add more songs in the Playlist for better experience."

    elif Total_duration > 3600:
        category = "Too Long Playlist"
        recommendation = "Remove some songs from the Playlist and make it balanced."

    elif repetitive:
        category = "Repetitive Playlist"
        recommendation = "Add variety."
    else:
        Duration_range = max(Playlist) - min(Playlist)
        if Duration_range <= 300:
            category = "Balanced Playlist"
            recommendation = "Good listening session"
        else:
            category = "Irregular Playlist"
            recommendation = "Try adjusting song durations"
    # Personalized Logic
    if Number_of_songs % 2 == 0:
        Listener_type = "Energetic Listener"
    else:
        Listener_type = "Calm Listener"

    print("\nTotal Duration:", Total_duration, "seconds")
    print("Number of Songs:", Number_of_songs)
    print("Category:", category)
    print("Recommendation:", recommendation)
    print("Listener Type:", Listener_type)