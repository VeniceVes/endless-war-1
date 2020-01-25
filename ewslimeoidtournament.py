import ewcfg
import ewutils
import ewslimeoid
import ewitem
from ew import EwUser
from ewmarket import EwMarket
from ewitem import EwItem
from ewplayer import EwPlayer

class EwSlimeoidTournament:
    id_server = ""

    #determines what's the status of the tournament(pre tournament, Winner's round 1, Loser's round 6, limbo, etc
    tournament_status = "SIGNUP"

    #number of brackets
    tournament_bracket = 4

    #current number of contestants
    contestants = 0

    #whether or not a losers bracket will be present
    losers_bracket = 0

    #number of slimeoids this tournament allows
    number_slimeoids = 1

    #how long a given set is, aka best 2 out of 3, best 3 out of 5, etc
    set_length = 3

    #if items are allowed
    tournament_items = 1

    #if steroids are allowed
    tournament_steroids = 0

    #if hues are allowed
    tournament_hues = 1

    #if candies are allowed
    tournament_candies = 0

    #if dyes are allowed(note: if hues aren't allowed, then neither or dyes
    tournament_dyes = 1

    #the minimum level a slimeoid can be
    level_min = 1

    #the maximum level a slimeoid can be
    level_max = 9

    #the tournament prize, probably a medallion or item
    reward = ""

    """ Load the slimeoid tournament data for this server from the database. """
    def __init__(self, id_server = None):
        if(id_server != None):
            self.id_server = id_server

            try:
                conn_info = ewutils.databaseConnect()
                conn = conn_info.get('conn')
                cursor = conn.cursor();

                # Retrieve object
                cursor.execute("SELECT {tournament_status}, {tournament_bracket}, {contestants}, {losers_bracket}, {number_slimeoids}, {set_length}, {tournament_items}, {tournament_steroids}, {tournament_hues}, {tournament_candies}, {tournament_dyes}, {level_min}, {level_max}, {reward}) FROM slimeoidtournaments WHERE id_server = %s".format(
                    tournament_status = ewcfg.col_tournament_status,
                    tournament_bracket = ewcfg.col_tournament_bracket,
                    contestants = ewcfg.col_contestants,
                    losers_bracket = ewcfg.col_losers_bracket,
                    number_slimeoids = ewcfg.col_number_slimeoids,
                    set_length = ewcfg.col_set_length,
                    tournament_items = ewcfg.col_tournament_items,
                    tournament_steroids = ewcfg.col_tournament_steroids,
                    tournament_hues = ewcfg.col_tournament_hues,
                    tournament_candies = ewcfg.col_tournament_candies,
                    tournament_dyes = ewcfg.col_tournament_dyes,
                    level_min = ewcfg.col_level_min,
                    level_max = ewcfg.col_level_max,
                    reward = ewcfg.col_reward,

                ), (self.id_server, ))
                result = cursor.fetchone();

                if result != None:
                    # Record found: apply the data to this object.
                    self.tournament_status = result[0]
                    self.tournament_bracket = result[1]
                    self.contestants = result[2]
                    self.losers_bracket = result[3]
                    self.number_slimeoids = result[4]
                    self.set_length = result[5]
                    self.tournament_items = result[6]
                    self.tournament_steroids = result[7]
                    self.tournament_hues = result[8]
                    self.tournament_candies = result[9]
                    self.tournament_dyes = result[10]
                    self.level_min = result[11]
                    self.level_max = result[12]
                    self.reward = result[13]

                else:
                    # Create a new database entry if the object is missing.
                    cursor.execute("REPLACE INTO slimeoidtournaments(id_server) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (id_server, ))

                    conn.commit()
            finally:
                # Clean up the database handles.
                cursor.close()
                ewutils.databaseClose(conn_info)

    """ Save slimeoid tournament data object to the database. """
    def persist(self):
        try:
            conn_info = ewutils.databaseConnect()
            conn = conn_info.get('conn')
            cursor = conn.cursor();

            # Save the object.
            cursor.execute("REPLACE INTO slimeoidtournaments ({id_server}, {tournament_status}, {tournament_bracket}, {contestants}, {losers_bracket}, {number_slimeoids}, {set_length}, {tournament_items}, {tournament_steroids}, {tournament_hues}, {tournament_candies}, {tournament_dyes}, {level_min}, {level_max}, {reward}) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)".format(
                id_server = ewcfg.col_id_server,
                tournament_status = ewcfg.col_tournament_status,
                tournament_bracket = ewcfg.col_tournament_bracket,
                contestants = ewcfg.col_contestants,
                losers_bracket = ewcfg.col_losers_bracket,
                number_slimeoids = ewcfg.col_number_slimeoids,
                set_length = ewcfg.col_set_length,
                tournament_items = ewcfg.col_tournament_items,
                tournament_steroids = ewcfg.col_tournament_steroids,
                tournament_hues = ewcfg.col_tournament_hues,
                tournament_candies = ewcfg.col_tournament_candies,
                tournament_dyes = ewcfg.col_tournament_dyes,
                level_min = ewcfg.col_level_min,
                level_max = ewcfg.col_level_max,
                reward = ewcfg.col_reward,
            ), (
                self.id_server,
                self.tournament_status,
                self.tournament_bracket,
                self.contestants,
                self.losers_bracket,
                self.number_slimeoids,
                self.set_length,
                self.tournament_items,
                self.tournament_steroids,
                self.tournament_hues,
                self.tournament_candies,
                self.tournament_dyes,
                self.level_min,
                self.level_max,
                self.reward,
            ))

            conn.commit()
        finally:
            # Clean up the database handles.
            cursor.close()
            ewutils.databaseClose(conn_info)

