import requests

API_KEY = 'myapikey'
API_BASE_URL = 'http://api.football-data.org/'
HEADERS = {'X-Auth-Token': API_KEY}

TEAM_CODES = {
    u'AFC Bournemouth': {
        'code': u'AFCB',
        'url': u'http://api.football-data.org/v1/teams/1044'},
    u'Arsenal FC': {
        'code': u'AFC',
        'url': u'http://api.football-data.org/v1/teams/57'},
    u'Aston Villa FC': {
        'code': u'AVFC',
        'url': u'http://api.football-data.org/v1/teams/58'},
    u'Chelsea FC': {
        'code': u'CFC',
        'url': u'http://api.football-data.org/v1/teams/61'},
    u'Crystal Palace FC': {
        'code': u'CRY',
        'url': u'http://api.football-data.org/v1/teams/354'},
    u'Everton FC': {
        'code': u'EFC',
        'url': u'http://api.football-data.org/v1/teams/62'},
    u'Leicester City FC': {
        'code': u'LCFC',
        'url': u'http://api.football-data.org/v1/teams/338'},
    u'Liverpool FC': {
        'code': u'LFC',
        'url': u'http://api.football-data.org/v1/teams/64'},
    u'Manchester City FC': {
        'code': u'MCFC',
        'url': u'http://api.football-data.org/v1/teams/65'},
    u'Manchester United FC': {
        'code': u'MUFC',
        'url': u'http://api.football-data.org/v1/teams/66'},
    u'Newcastle United FC': {
        'code': u'NUFC',
        'url': u'http://api.football-data.org/v1/teams/67'},
    u'Norwich City FC': {
        'code': u'NCFC',
        'url': u'http://api.football-data.org/v1/teams/68'},
    u'Southampton FC': {
        'code': u'SFC',
        'url': u'http://api.football-data.org/v1/teams/340'},
    u'Stoke City FC': {
        'code': u'SCFC',
        'url': u'http://api.football-data.org/v1/teams/70'},
    u'Sunderland AFC': {
        'code': u'SUN',
        'url': u'http://api.football-data.org/v1/teams/71'},
    u'Swansea City FC': {
        'code': u'SWA',
        'url': u'http://api.football-data.org/v1/teams/72'},
    u'Tottenham Hotspur FC': {
        'code': u'THFC',
        'url': u'http://api.football-data.org/v1/teams/73'},
    u'Watford FC': {
        'code': u'Watfordfc',
        'url': u'http://api.football-data.org/v1/teams/346'},
    u'West Bromwich Albion FC': {
        'code': u'WBA',
        'url': u'http://api.football-data.org/v1/teams/74'},
    u'West Ham United FC': {
        'code': u'WHU',
        'url': u'http://api.football-data.org/v1/teams/563'}}

TEAM_CODE_DICT = dict([(team_data.get('code'), team_name) for team_name, team_data in TEAM_CODES.items()])


def getTeams():
    url = 'v1/soccerseasons/398/teams'
    response = requests.get(API_BASE_URL + url, headers=HEADERS)
    teams = {}
    for team in response.json().get('teams'):
        teams[team.get('name')] = {
            'code': team.get('code'),
            'url': team.get('_links').get('self').get('href'),
        }
    return teams


def getTeamInfo(url):
    response = requests.get(url, headers=HEADERS)
    return response.json()

def getTable():
    url = 'v1/soccerseasons/398/leagueTable'
    response = requests.get(API_BASE_URL + url, headers=HEADERS)
    table = []
    for team in response.json().get('standing'):
        print team.keys()
        table.append([team.get('teamName'), team.get('wins'), team.get(
            'draws'), team.get('losses'), team.get('points')])
    return table

if __name__ == '__main__':
    # table = getTable()
    lfc = TEAM_CODE_DICT.get('LFC')
    print getTeamInfo(TEAM_CODES.get(lfc).get('url'))
