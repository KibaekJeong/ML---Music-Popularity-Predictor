#!/usr/bin/env python
# coding: utf-8

# In[31]:


import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from IPython.display import display
import numpy as np
from array import array
from scipy.stats import kurtosis
from scipy.stats import entropy


# In[32]:


def get_song_info(track_id):
    # Using Client Credentials for authorization
    client_credentials_manager = SpotifyClientCredentials(client_id="f2d11bfce2cf4bae8e096454ca4299ed",client_secret="0192b251aff04567a49d33d83287a254")
    sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
    # get access token for spotify
    token = client_credentials_manager.get_access_token()
    data = []
    track_info = sp.track(track_id)
    artists = track_info['artists']
    track_popularity = track_info['popularity']
    track_name = track_info['name']
    #get artist info
    artist = []
    for item in range(0,len(artists)):
        artist_id = artists[item]['id']
        artist_name = artists[item]['name']
        artist_info = sp.artist(artist_id)
        artist_popularity = artist_info['popularity']
        artist_follower = artist_info['followers']['total']
        artist.append({'artist_name':artist_name,'artist_id':artist_id,'artist_popularity':artist_popularity,'artist_followers':artist_follower})
    more_popular = 0
    for item in range(0,len(artist)):
        if artist[item]['artist_popularity'] > more_popular:
            more_popular_index = item
            more_popular = artist[item]['artist_popularity']
    # Get audio analytical data
            audio_analysis = sp.audio_analysis(track_id)
            audio_section_data = audio_analysis['sections']

            weight = []
            confidence = []
            loudness = []
            tempo = []
            tempo_confidence = []
            key = []
            key_confidence = []
            mode = []
            mode_confidence = []
            time_signature = []
            time_signature_confidence = []

            #rearrange sectional audio analysis dataset for computation
            for item in range(0,len(audio_analysis['sections'])):
                # Note: weight = duration of each section
                weight.append(audio_analysis['sections'][item]['duration'])
                confidence.append(audio_analysis['sections'][item]['confidence'])
                loudness.append(audio_analysis['sections'][item]['loudness'])
                tempo.append(audio_analysis['sections'][item]["tempo"])
                tempo_confidence.append(audio_analysis['sections'][item]["tempo_confidence"])
                key.append(audio_analysis['sections'][item]['key'])
                key_confidence.append(audio_analysis['sections'][item]['key_confidence'])
                mode.append(audio_analysis['sections'][item]['mode'])
                mode_confidence.append(audio_analysis['sections'][item]['mode_confidence'])
                time_signature.append(audio_analysis['sections'][item]['time_signature'])
                time_signature_confidence.append(audio_analysis['sections'][item]['time_signature_confidence'])

            #balancing data as each section has different duration 
            average_duration = np.average(weight)
            balancing_coeff = np.array(weight)/average_duration
            balanced_data = []
            balanced_data.append(confidence*balancing_coeff)
            balanced_data.append(loudness*balancing_coeff)
            balanced_data.append(tempo*balancing_coeff)
            balanced_data.append(tempo_confidence*balancing_coeff)
            balanced_data.append(key*balancing_coeff)
            balanced_data.append(key_confidence*balancing_coeff)
            balanced_data.append(mode*balancing_coeff)
            balanced_data.append(mode_confidence*balancing_coeff)
            balanced_data.append(time_signature*balancing_coeff)
            balanced_data.append(time_signature_confidence*balancing_coeff)


            #get mean, standard deviation, and kurtosis for each data
            calculated_data = []
            for item in range(0,len(balanced_data)):
                section = array('f')
                for i in range(0,len(balanced_data[item])):
                    section.append(balanced_data[item][i])
                section_kur = kurtosis(section)
                mean = np.mean(balanced_data[item])
                std = np.std(balanced_data[item])
                calculated_data.append([mean,std,section_kur])

            audio_segment_data = audio_analysis['segments']
            pitch1 = []
            pitch2 = []
            pitch3 = []
            pitch4 = []
            pitch5 = []
            pitch6 = []
            pitch7 = []
            pitch8 = []
            pitch9 = []
            pitch10 = []
            pitch11 = []
            pitch12 = []
            timbre1 = []
            timbre2 = []
            timbre3 = []
            timbre4 = []
            timbre5 = []
            timbre6 = []
            timbre7 = []
            timbre8 = []
            timbre9 = []
            timbre10 = []
            timbre11 = []
            timbre12 = []
            weight_seg = []

            for item in range(0,len(audio_analysis['segments'])):
                weight_seg.append(audio_analysis['segments'][item]['duration'])
                pitch1.append(audio_analysis['segments'][item]['pitches'][0])
                pitch2.append(audio_analysis['segments'][item]['pitches'][1])
                pitch3.append(audio_analysis['segments'][item]['pitches'][2])
                pitch4.append(audio_analysis['segments'][item]['pitches'][3])
                pitch5.append(audio_analysis['segments'][item]['pitches'][4])
                pitch6.append(audio_analysis['segments'][item]['pitches'][5])
                pitch7.append(audio_analysis['segments'][item]['pitches'][6])
                pitch8.append(audio_analysis['segments'][item]['pitches'][7])
                pitch9.append(audio_analysis['segments'][item]['pitches'][8])
                pitch10.append(audio_analysis['segments'][item]['pitches'][9])
                pitch11.append(audio_analysis['segments'][item]['pitches'][10])
                pitch12.append(audio_analysis['segments'][item]['pitches'][11])
                timbre1.append(audio_analysis['segments'][item]['timbre'][0])
                timbre2.append(audio_analysis['segments'][item]['timbre'][1])
                timbre3.append(audio_analysis['segments'][item]['timbre'][2])
                timbre4.append(audio_analysis['segments'][item]['timbre'][3])
                timbre5.append(audio_analysis['segments'][item]['timbre'][4])
                timbre6.append(audio_analysis['segments'][item]['timbre'][5])
                timbre7.append(audio_analysis['segments'][item]['timbre'][6])
                timbre8.append(audio_analysis['segments'][item]['timbre'][7])
                timbre9.append(audio_analysis['segments'][item]['timbre'][8])
                timbre10.append(audio_analysis['segments'][item]['timbre'][9])
                timbre11.append(audio_analysis['segments'][item]['timbre'][10])
                timbre12.append(audio_analysis['segments'][item]['timbre'][11])


            average_duration_seg = np.average(weight_seg)
            balancing_coeff_seg = np.array(weight_seg)/average_duration_seg
            pitch_balanced_data = []
            timbre_balanced_data = []
            pitch_balanced_data.append(pitch1*balancing_coeff_seg)
            pitch_balanced_data.append(pitch2*balancing_coeff_seg) 
            pitch_balanced_data.append(pitch3*balancing_coeff_seg) 
            pitch_balanced_data.append(pitch4*balancing_coeff_seg) 
            pitch_balanced_data.append(pitch5*balancing_coeff_seg) 
            pitch_balanced_data.append(pitch6*balancing_coeff_seg) 
            pitch_balanced_data.append(pitch7*balancing_coeff_seg) 
            pitch_balanced_data.append(pitch8*balancing_coeff_seg) 
            pitch_balanced_data.append(pitch9*balancing_coeff_seg) 
            pitch_balanced_data.append(pitch10*balancing_coeff_seg) 
            pitch_balanced_data.append(pitch11*balancing_coeff_seg) 
            pitch_balanced_data.append(pitch12*balancing_coeff_seg) 
            timbre_balanced_data.append(timbre1*balancing_coeff_seg)  
            timbre_balanced_data.append(timbre2*balancing_coeff_seg)
            timbre_balanced_data.append(timbre3*balancing_coeff_seg)
            timbre_balanced_data.append(timbre4*balancing_coeff_seg)
            timbre_balanced_data.append(timbre5*balancing_coeff_seg)
            timbre_balanced_data.append(timbre6*balancing_coeff_seg)
            timbre_balanced_data.append(timbre7*balancing_coeff_seg)
            timbre_balanced_data.append(timbre8*balancing_coeff_seg)
            timbre_balanced_data.append(timbre9*balancing_coeff_seg)
            timbre_balanced_data.append(timbre10*balancing_coeff_seg)
            timbre_balanced_data.append(timbre11*balancing_coeff_seg)
            timbre_balanced_data.append(timbre12*balancing_coeff_seg)

            #get statistics for pitch,
            pitch_data = []
            total = []
            for item in range(0,len(pitch_balanced_data)):
                segment_pitch = array('f')
                for i in range(0,len(pitch_balanced_data[item])):
                    segment_pitch.append(pitch_balanced_data[item][i])
                mean = np.mean(pitch_balanced_data[item])
                std = np.std(pitch_balanced_data[item])
                total.append(sum(pitch_balanced_data[item]))
                iqr_pit_75 = np.percentile(pitch_balanced_data[item],75)
                iqr_pit_25 = np.percentile(pitch_balanced_data[item],25)
                iqr_pit = iqr_pit_75 - iqr_pit_25
                seg_pit_kurtosis = kurtosis(segment_pitch)
                pitch_data.append([mean,std,iqr_pit,seg_pit_kurtosis])

            pitch_percentile = [x/sum(total) for x in total]
            pitch_entropy = entropy(pitch_percentile)


            #get statistics for timbre
            timbre_data = []
            total = []
            for item in range(0,len(timbre_balanced_data)):
                segment_timbre = array('f')
                for i in range(0,len(timbre_balanced_data[item])):
                    segment_timbre.append(timbre_balanced_data[item][i])
                mean = np.mean(timbre_balanced_data[item])
                std = np.std(timbre_balanced_data[item])
                total.append(sum(timbre_balanced_data[item]))
                iqr_tim_75 = np.percentile(timbre_balanced_data[item],75)
                iqr_tim_25 = np.percentile(timbre_balanced_data[item],25)
                iqr_tim = iqr_tim_75 - iqr_tim_25
                seg_tim_kurtosis = kurtosis(segment_timbre)
                timbre_data.append([mean,std,iqr_tim,seg_tim_kurtosis])

            timbre_percentile = [x/sum(total) for x in total]
            timbre_entropy = entropy(timbre_percentile)
            data.append({"track_name":track_name,"artist_name":artist[more_popular_index]['artist_name'],                             "track_id":track_id,"artist_id":artist[more_popular_index]["artist_id"],                             "track_popularity":track_popularity,"artist_popularity":artist[more_popular_index]["artist_popularity"],                             "artist_followers":artist[more_popular_index]["artist_followers"],"confidence_mean":calculated_data[0][0],                             "confidence_std":calculated_data[0][1],"confidence_kurtosis":calculated_data[0][2],"loudness_mean":calculated_data[1][0],                             "loudness_std":calculated_data[1][1],"loudness_kurtosis":calculated_data[1][2],"tempo_mean":calculated_data[2][0],                             "tempo_std":calculated_data[2][1],"tempo_kurtosis":calculated_data[2][2],"tempo_confidence_mean":calculated_data[3][0],                             "tempo_confidence_std":calculated_data[3][1],"tempo_confidence_kurtosis":calculated_data[3][2],"key_mean":calculated_data[4][0],                             "key_std":calculated_data[4][1],"key_kurtosis":calculated_data[4][2],"key_confidence_mean":calculated_data[5][0],                             "key_confidence_std":calculated_data[5][1],"key_confidence_kurtosis":calculated_data[5][2],"mode_mean":calculated_data[6][0],                             "mode_std":calculated_data[6][1],"mode_kurtosis":calculated_data[6][2],"mode_confidence_mean":calculated_data[7][0],                             "mode_confidence_std":calculated_data[7][1],"mode_confidence_kurtosis":calculated_data[7][2],                              "time_signature_mean":calculated_data[8][0],"time_signature_std":calculated_data[8][1],"time_signature_kurtosis":calculated_data[8][2],                             "time_signature_confidence_mean":calculated_data[9][0],"time_signature_confidence_std":calculated_data[9][1],                             "time_signature_confidence_kurtosis":calculated_data[9][2],"C_dominance_mean":pitch_data[0][0],"C_dominance_std":pitch_data[0][1],                             "C_dominance_iqr":pitch_data[0][2],"C_dominance_kurtosis":pitch_data[0][3],"C#_dominance":pitch_data[1][0],"C#_dominance_std":pitch_data[1][1],                             "C#_dominance_iqr":pitch_data[1][2],"C#_dominance_kurtosis":pitch_data[1][3],"D_dominance_mean":pitch_data[2][0],                             "D_dominance_std":pitch_data[2][1],"D_dominance_iqr":pitch_data[2][2], "D_dominance_kurtosis":pitch_data[2][3],                             "D#_dominance_mean":pitch_data[3][0],"D#_dominance_std":pitch_data[3][1],"D#_dominance_iqr":pitch_data[3][2],"D#_dominance_kurtosis":pitch_data[3][3],                             "E_dominance_mean":pitch_data[4][0],"E_dominance_std":pitch_data[4][1],"E_dominance_iqr":pitch_data[4][2],"E_dominance_kurtosis":pitch_data[4][3],                             "F_dominance_mean":pitch_data[5][0],"F_dominance_std":pitch_data[5][1],"F_dominance_iqr":pitch_data[5][2],"F_dominance_kurtosis":pitch_data[5][3],                             "F#_dominance_mean":pitch_data[6][0],"F#_dominance_std":pitch_data[6][1],"F#_dominance_iqr":pitch_data[6][2],"F#_dominance_kurtosis":pitch_data[6][3],                             "G_dominance_mean":pitch_data[7][0],"G_dominance_std":pitch_data[7][1],"G_dominance_iqr":pitch_data[7][2],"G_dominance_kurtosis":pitch_data[7][3],                             "G#_dominance_mean":pitch_data[8][0],"G#_dominance_std":pitch_data[8][1],"G#_dominance_iqr":pitch_data[8][2],"G#_dominance_kurtosis":pitch_data[8][3],                             "A_dominance_mean":pitch_data[9][0],"A_dominance_std":pitch_data[9][1],"A_dominance_iqr":pitch_data[9][2],"A_dominance_kurtosis":pitch_data[9][3],                             "A#_dominance_mean":pitch_data[10][0],"A#_dominance_std":pitch_data[10][1],"A#_dominance_iqr":pitch_data[10][2],"A#_dominance_kurtosis":pitch_data[10][3],                             "B_dominance_mean":pitch_data[11][0],"B_dominance_std":pitch_data[11][1],"B_dominance_iqr":pitch_data[11][2],"B_dominance_kurtosis":pitch_data[11][3],                             "pitch_entropy":pitch_entropy,"timbre_1_mean":timbre_data[0][0],"timbre_1_std":timbre_data[0][1],                             "timbre_1_iqr":timbre_data[0][2],"timbre_1_kurtosis":timbre_data[0][3],"timbre_2_mean":timbre_data[1][0],"timbre_2_std":timbre_data[1][1],                             "timbre_2_iqr":timbre_data[1][2],"timbre_2_kurtosis":timbre_data[1][3],"timbre_3_mean":timbre_data[2][0],                             "timbre_3_std":timbre_data[2][1],"timbre_3_iqr":timbre_data[2][2],"timbre_3_kurtosis":timbre_data[2][3],                             "timbre_4_mean":timbre_data[3][0],"timbre_4_std":timbre_data[3][1],"timbre_4_iqr":timbre_data[3][2],"timbre_4_kurtosis":timbre_data[3][3],                             "timbre_5_mean":timbre_data[4][0],"timbre_5_std":timbre_data[4][1],"timbre_5_iqr":timbre_data[4][2],"timbre_5_kurtosis":timbre_data[4][3],                             "timbre_6_mean":timbre_data[5][0],"timbre_6_std":timbre_data[5][1],"timbre_6_iqr":timbre_data[5][2],"timbre_6_kurtosis":timbre_data[5][3],                             "timbre_7_mean":timbre_data[6][0],"timbre_7_std":timbre_data[6][1],"timbre_7_iqr":timbre_data[6][2],"timbre_7_kurtosis":timbre_data[6][3],                             "timbre_8_mean":timbre_data[7][0],"timbre_8_std":timbre_data[7][1],"timbre_8_iqr":timbre_data[7][2],"timbre_8_kurtosis":timbre_data[7][3],                             "timbre_9_mean":timbre_data[8][0],"timbre_9_std":timbre_data[8][1],"timbre_9_iqr":timbre_data[8][2],"timbre_9_kurtosis":timbre_data[8][3],                             "timbre_10_mean":timbre_data[9][0],"timbre_10_std":timbre_data[9][1],"timbre_10_iqr":timbre_data[9][2],"timbre_10_kurtosis":timbre_data[9][3],                             "timbre_11_mean":timbre_data[10][0],"timbre_11_std":timbre_data[10][1],"timbre_11_iqr":timbre_data[10][2],"timbre_11_kurtosis":timbre_data[10][3],                             "timbre_12_mean":timbre_data[11][0],"timbre_12_std":timbre_data[11][1],"timbre_12_iqr":timbre_data[11][2],"timbre_12_kurtosis":timbre_data[11][3],                             "timbre_entropy":timbre_entropy})
    return data


# In[ ]:




