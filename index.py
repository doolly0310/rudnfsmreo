import discord
import random
import os

access_token=os.environ["BOT_TOKEN"]
client = discord.Client()

token =access_token

@client.event
async def on_ready():
    print('Client is Ready')

@client.event
async def on_message(message):
    if message.content == '/호드 아이오': 
        await message.channel.send('음 그 쪽지는....(구겨진 종이를 꺼냄)https://hordes.io/ 여기있다! 잘 꺼낸 건가?')
    elif message.content == '/으아악': 
        await message.channel.send('ㅋㅋㅋ')
    elif message.content == '/검색':
        await message.channel.send('난 할수있는게 https://www.naver.com/ 이거 소환하는거야')
    elif message.content == '/시작해':
        await message.channel.send('끝났어')
    elif message.content == '/크시':
        await message.channel.send('나,겨울늑대나 같은 늑대!')
    elif message.content == '/게임':
        await message.channel.send('HORDES.IO 열때는 /호드 아이오나 /홀뎃을, 파리게임 열때는 /파리를, 땅따먹기 할땐 /종이를...')
    elif message.content == '/파리':
        await message.channel.send('재미있는 파리를 하려고? 잠깐만....https://evoworld.io/play?loc=AUS 이거야?')
    elif message.content == '/하품':
        await message.channel.send('아함 (하품을 한다.)')
    elif message.content == '/배추봇':
        await message.channel.send('마이펫') 
    elif message.content == '/홀뎃':
        await message.channel.send('음... 알았어 이 종이는 잘 부서져!(구겨진 종이를 꺼냄) https://hordes.io/ 이건데..')
    elif message.content == '아함':
        await message.channel.send('지루해? 그럼 버튼을 누르고 스네이크 게임을 하지? 돼지 옆 파란버튼 누르면 돼. 읏차 https://discord.com/%EB%8F%BC%EC%A7%80%EC%98%86%20%ED%8C%8C%EB%9E%80%EB%B2%84%ED%8A%BC%20%EB%88%84%EB%A5%B4%EC%8B%9C%EB%A9%B4%20snek%EB%9D%BC%EB%8A%94%20%EB%B1%80%EA%B2%8C%EC%9E%84%EC%9D%B4%20%EB%82%98%EC%98%B4')
    elif message.content == '/ㅋㅋㅋ':
        await message.channel.send('으아악')
    elif message.content == '/ㄷㄷㄷ':
        await message.channel.send('무서워')  
    elif message.content == '/하고싶은 말은?':
        await message.channel.send('빨리 나가')  
    elif message.content == '/개발자':
        await message.channel.send('겨울늑대가 날 만들었지! 너....설마 겨울늑대인가?')
    elif message.content == '/뛰어':
        await message.channel.send('배고파......(겨울늑대 말곤 날 뛰게 못해)')
    elif message.content == '/밥':  
        await message.channel.send('(허겁지겁 아구아구)다 먹었다.||더 주지...제발...||')  
    elif message.content == '/메시지 폭탄':  
        await message.channel.send('ㅏ저ㅗ루ㅡ투ㅠㅍㅇㅀㅇ횽ㅍㅊㅎㅇㅎㅀㅍㅇㅎㅇㅎㅎㅎㄹ퓨퓨휴류ㅗㅎㅎ퓨흃류류ㅠㅠ(돈 -1000000원')  
    elif message.content == '/자':
        await message.channel.send('(이미 자고 있었음) zzz.....')
    elif message.content == '/똥':
        await message.channel.send('뿌지직')
    elif message.content == '/앉아':
        await message.channel.send('(앉음)')
    elif message.content == '/욕해':
        await message.channel.send(':face_with_symbols_over_mouth: 이정도면 됐지? 더 심하겐 안해')
    elif message.content == '/누워':
        await message.channel.send('(누움...그러다 zzz)')
    elif message.content == '/늑대': 
        await message.channel.send('나...? 아니면 겨울늑대....?')
    elif message.content == '/미육':
        await message.channel.send('가지고 공놀이 하자!')
    elif message.content == '/늑대야 ㅎㅇ':
        await message.channel.send('ㅇㅇ ㅎㅇ')
    elif message.content == '/공놀이':
        await message.channel.send('(1번 던져주고 받고...1000번 던져주고 받고...) 더 해줘!')
    elif message.content == '/늑대야 ㅂ2':
        await message.channel.send('벌써? 잘가~~')
    elif message.content == '/불쌍해':
        await message.channel.send('왜? 난 안 불쌍해!')
    elif message.content == '/한번 때려봐':
        await message.channel.send('그윽(발톱으로 얼굴을 할큄(특히 늑대가...))')
    elif message.content == '/지워':
        await message.channel.send('마력은 한 10억년만 있으면 모두 회복될거야 그때까지만 참아줘')
    elif message.content == '/수정구슬':
        await message.channel.send('한번 보자...')
        seedNum=random.randrange(1,5)
        if seedNum==1:
            await message.channel.send('(최악의 하루가 예상됩니다.)근데 마력을 다 써버렸...(기절)')
        elif seedNum==2:
            await message.channel.send('(엄청난 운이 예상됩니다.)오 엄청나군!근데 마력을 다 써버렸...(기절)')
        elif seedNum==3:
            await message.channel.send('(운이 별로 좋지 않은 하루가 예상됩니다.)음... 그다지 좋진 않겠군.근데 마력을 다 써버렸...(기절)')
        elif seedNum==4:
            await message.channel.send('(오늘은 운이 아주 좋아요! 게임이면 오류로 10레벨이 올라갈 수도 있고요!)오 운이 아주 좋군!근데 마력을 다 써버렸...(기절)')    
        elif seedNum==5:
            await message.channel.send('(오늘은 아주 운이 없네요! 아주 안좋은 하루가 예상됩니다.)이런 너 오늘 망쳤어.근데 마력을 다 써버렸...(기절)')    
    elif message.content == '/종이':
        await message.channel.send('일반 할거면 /종이2를,팀모드 할거면 /종이 팀을,나라모드 할거면 /종이나라를 말해줘')
    elif message.content == '/종이2':
        await message.channel.send('https://paper-io.com/ 이거야 들어가!')
    elif message.content == '/종이 팀':
        await message.channel.send('https://paper-io.com/teams/ 네가 그걸 고를지 몰랐는데')
    elif message.content == '/종이나라':
        await message.channel.send('https://paper-io.com/conflict/ 윽....마력을 다 써버렸어(기절)')
    elif message.content == '/마력충전':
        await message.channel.send('겨울늑대가 해주면 모를까 내가하면 10억년 걸려')
    elif message.content == '/돈':
        await message.channel.send('뭐야 100000경루도 없는게 나한테 니 돈을 알려달래')
    elif message.content == '/얼마있어':
        await message.channel.send('난 정확히 100000경루가 있어')
    elif message.content == '/끝말잇기':
        await message.channel.send('그건 크시랑 해 나 귀찮게 하지말고. 만약 겨울늑대가 만들어주면 모를까')
    elif message.content == '/좋아하는 음식은?':
        await message.channel.send('개 간식...이 아니라 난 늑대니까 늑대간식')
    elif message.content == '/잘자':
        await message.channel.send('그래 악어(유저)야 너두 잘자. 혹시 겨울늑대면... 잘자 늑대야')
    elif message.content == '/출첵':
        await message.channel.send('출석..... ㅇ 니 출첵')
    elif message.content == '/번역기':
        await message.channel.send('잠깐만 있어봐.. 내가 번역기좀 줄게 최신형이야 읏차 https://papago.naver.com/ 이거!')
    elif message.content == '/도움말':
        embed = discord.Embed(title = '도움말', description = '대화를 하려면 /친뒤 말해(아함 빼고)', color = discord.Color.blue())
        embed.add_field(name = '도움말은...', value = '/게임,/수정구슬,/번역기,/검색/출첵,/돈,/얼마있어,/하품,/마력충전,/지워,아함,/좋아하는 음식은?,/끝말잇기,/한번 때려봐,/잘자,/미육,/공놀이,/늑대야 ㅂ2,/욕해 등.... 아직 남았지만... 나중에 추가할게요-겨울늑대- ')
        await message.channel.send(embed = embed)
    elif message.content ==  '/난 9999조 경루 있는데 어쩔거냐'
        await message.channel.send('최신형 차나 1조개  ')
client.run(token)
