# -*- coding: utf-8 -*-
import random
import aiohttp
import discord
from discord.ext import commands
from discord_components import DiscordComponents, Button, ButtonStyle
papichgif =[
    "https://c.tenor.com/Xl5AoPPfQbIAAAAd/%D0%BF%D0%B0%D0%BF%D0%B8%D1%87-%D0%B2%D0%B5%D0%BB%D0%B8%D1%87%D0%B0%D0%B9%D1%88%D0%B8%D0%B9.gif",
    "https://i.pinimg.com/originals/9b/ed/2e/9bed2e062948e0a2950b6cdfdb1310c3.gif"
    "https://media.tenor.com/e5-vmCtRTQ8AAAAd/%D0%BF%D0%B0%D0%BF%D0%B8%D1%87-arthas.gif"
    "https://media.tenor.com/74QM2zVnaiMAAAAd/papich-%D0%BF%D0%B0%D0%BF%D0%B8%D1%87.gif"
    "https://media.tenor.com/dnTNlgOnLzsAAAAC/%D0%BF%D0%B0%D0%BF%D0%B8%D1%87-dance.gif"
]
papizi =[
"https://yt3.ggpht.com/QVYMnZM7t2mWxA6PoOwFHntynX5TwQU1VVtYJySTwZZ7LSttru6n4ipOUOrmaWU93sPZccnuXw=s900-c-k-c0x00ffffff-no-rj",
"https://img.playbuzz.com/image/upload/ar_1.5,c_crop/q_auto:good,f_auto,fl_lossy,w_640,c_limit,dpr_2.5/v1592660782/etppeodnp6sbl0bbd67h",
"https://games-walker.com/wp-content/uploads/2020/12/Papych-Vse-pro-Papycha.jpg"
]
variantinastoeninorm = ["нормально", "средне","плюс-минус","+-","так себе","норм"]
variantinastoeniebad =["плохо","что то не очень","sad","тильт","не очень","плоховато","печально"]
variantinastoeniagood=["хорошо", "отлично","прекрасно","супер","гуд","ультрамеганорм","ультрамегахарош","найс","нойс"]
variatiprivetov = [
    "ку бот","хай бот","привет бот","здарова бот","доброе утро бот","здраствуй бот"
]


varianti = [
    'Пуск',
    'На старт',
    'Погнали'
]
config = {
    'token': 'ODI5MjQzNzM5Nzc5MTA0ODE4.GGi39l.Is3QpKXqq0QJlKIYRNop1jt4xiuhr_Y1tupYgQ',
    'prefix': '!',
}

bot = commands.Bot(command_prefix=config['prefix'])


@bot.event
async def on_ready():
    DiscordComponents(bot)
    print(random.choice(varianti))
    await bot.change_presence(status=discord.Status.online,activity=discord.Game("Антитильт"))













    @bot.command()
    async def kvest(ctx):
        v=0
        b=0
        s=0
        await ctx.send(
            embed=discord.Embed(title="Играем?"),
            components=[
                Button(style=ButtonStyle.green, label="Агась"),
                Button(style=ButtonStyle.red, label="Не"),
            ]
        )
        responce = await bot.wait_for("button_click")
        if responce.component.label == "Не":
            await responce.respond(embed=discord.Embed(title="Ты злюкааа"),
                                   components=[
                    Button(style=ButtonStyle.blue, label="Продолжить"),

                ]),
        if responce.component.label == "Агась":
            await responce.respond(embed=discord.Embed(title="Предистория"),
                                   components=[
                    Button(style=ButtonStyle.blue, label="Продолжить"),

                ]),
        responce = await bot.wait_for("button_click")
        if responce.component.label == "Продолжить":
                await responce.respond(
                    embed=discord.Embed(title="Я проснулся около 8:00, достаточно рано для меня. Хм, неужели и вправду нервишки шалят. Сегодня  ответственный день, последний тест системы до автономного запуска.И конечно же его должен провести я."),
                    components=[
                        Button(style=ButtonStyle.blue, label="Продолжить"),

                    ]),
        responce = await bot.wait_for("button_click")
        if responce.component.label == "Продолжить":
            await responce.respond(
                embed=discord.Embed(title="Какая чепуха, почему именно я должен проводить последний тест? Я уверен в работоспособности системы так как она уже далеко не первая, а тест может провести любой из моих коллег"),
                components=[
                    Button(style=ButtonStyle.blue, label="Продолжить"),
]),
        responce = await bot.wait_for("button_click")
        if responce.component.label == "Продолжить":
            await responce.respond(
                embed=discord.Embed(
                    title="Умылся, позавтракал, собрал вещи и перед выходом окинул взором свою типичную однушку. «Ха, а ведь если проект выгорит смогу перебраться в квартирку попрестижней»- пролетело у меня в голове. "),
                components=[
                    Button(style=ButtonStyle.blue, label="Продолжить"),
                ]),
        responce = await bot.wait_for("button_click")
        if responce.component.label == "Продолжить":
            await responce.respond(
                embed=discord.Embed(
                    title="У меня в запасе минут 20, может захватить воды? "),
                components=[
                    Button(style=ButtonStyle.green, label="Взять воды"),
                    Button(style=ButtonStyle.red, label="Не идти за водой"),
                ]),
        responce = await bot.wait_for("button_click")
        if responce.component.label == "Взять воды":
            v=v+1
            await responce.respond(embed=discord.Embed(title="«Почему бы и нет»- подумал я, и зашел в ближайших продуктовый рады бутылки живительной H2O. «Может пригодится» ."),
                                   components=[
                                       Button(style=ButtonStyle.blue, label="Продолжить"),

                                   ]),
        if responce.component.label == "Не идти за водой":
            await responce.respond(embed=discord.Embed(title="А собственно зачем? Сейчас мне не нужно, а на работе я по любому найду что попить или у кого попросить. За то приеду с небольшим запасом по времени"),
                                   components=[
                                       Button(style=ButtonStyle.blue, label="Продолжить"),
                                   ]),
        responce = await bot.wait_for("button_click")
        if responce.component.label == "Продолжить":
            await responce.respond(
                embed=discord.Embed(
                    title="«Вызвать такси или как обычно воспользоваться метро?». "),
                components=[
                    Button(style=ButtonStyle.green, label="Метро"),
                    Button(style=ButtonStyle.red, label="Такси"),
                ]),
        responce = await bot.wait_for("button_click")
        if responce.component.label == "Метро":
            await responce.respond(embed=discord.Embed(
                title="«Ха, с чего бы? Как будто бы таксист узнав что именно сегодня решающий тест Alife отвезет меня бесплатно. Поедем по старинке, нечего тратится по пустякам»."),
                                   components=[
                                       Button(style=ButtonStyle.blue, label="Продолжить"),

                                   ]),
        if responce.component.label == "Такси":
            await responce.respond(embed=discord.Embed(
                title="Несмотря на мое скептическое отношение к «особенности»  данного дня. Воспользоваться этим как оправдание поездки на такси мне очень хотелось, так что подождав такси минут 10 , я уже мчался к рабочему месту"),
                                   components=[
                                       Button(style=ButtonStyle.blue, label="Продолжить"),
                                   ]),
        responce = await bot.wait_for("button_click")
        if responce.component.label == "Продолжить":
            await responce.respond(
                embed=discord.Embed(
                    title="Как бы вы представили офис ведущей компании по разработке AI? Небоскрёб полон стеклянных стен? Возможно огромное подвальное помещение? Обычное пятиэтажное здание с потолками 2,5 метра."),
                components=[
                    Button(style=ButtonStyle.blue, label="Продолжить"),
                ]),
        responce = await bot.wait_for("button_click")
        if responce.component.label == "Продолжить":
            await responce.respond(
                embed=discord.Embed(
                    title="Скорее напоминающие заброшенный завод чем офис. Всё по заветам серпа и молота.Впрочем внутри всё не так плачевно как снаружи, так что жаловатся толком не на что."),
                components=[
                    Button(style=ButtonStyle.blue, label="Продолжить"),
                ]),
        responce = await bot.wait_for("button_click")
        if responce.component.label == "Продолжить":
            await responce.respond(
                embed=discord.Embed(
                    title="Войдя в здание я обнаружил что оно пустое. С одной стороны я прибыл достаточно рано и отсутствие сотрудников вполне ожидаемо. С другой стороны Кир на ресепшн уже должен был приехать."),
                components=[
                    Button(style=ButtonStyle.blue, label="Продолжить"),
                ]),

        responce = await bot.wait_for("button_click")
        if responce.component.label == "Продолжить":
            await responce.respond(
                embed=discord.Embed(
                    title="Нужно отбросить мысли что кто то из ребят мог проспать или банально забыть про необходимость именно сегодня быть на работе ВОВРЕМЯ, а лучше заранее."),
                components=[
                    Button(style=ButtonStyle.blue, label="Продолжить"),
                ]),
        responce = await bot.wait_for("button_click")
        if responce.component.label == "Продолжить":
            await responce.respond(
                embed=discord.Embed(
                    title="Разложив вещи на своем столе, проверил работоспособность Alife ,и понаблюдав за логами несколько минут не увидел ошибок\ критических отхождений от нормы, и принялся ждать остальных."),
                components=[
                    Button(style=ButtonStyle.blue, label="Продолжить"),
                ]),
        responce = await bot.wait_for("button_click")
        if responce.component.label == "Продолжить":
            await responce.respond(
                embed=discord.Embed(
                    title="Собственно прибыть должны Кир(молодой парень, работает с нами от силы месяцев 5,принимает гостей на ресепшене и в свободное время учится у остальных)"),
                components=[
                    Button(style=ButtonStyle.blue, label="Продолжить"),
                ]),
        responce = await bot.wait_for("button_click")
        if responce.component.label == "Продолжить":
            await responce.respond(
                embed=discord.Embed(
                    title="Яр он же Яромир(специалист по кодировке,шифрованию,информационной безопасности проекта и одновременной мой заместитель по контролю качества) и Раст(младший сотрудник контроля отдела качества)."),
                components=[
                    Button(style=ButtonStyle.blue, label="Продолжить"),
                ]),
        responce = await bot.wait_for("button_click")
        if responce.component.label == "Продолжить":
            await responce.respond(
                embed=discord.Embed(
                    title="Сотрудников в компании намного больше, но из пятиэтажного здание на нашем, а именно 3 этаже я перечислил всех. "),
                components=[
                    Button(style=ButtonStyle.blue, label="Продолжить"),
                ]),
        responce = await bot.wait_for("button_click")
        if responce.component.label == "Продолжить":
            await responce.respond(
                embed=discord.Embed(
                    title="Задачи на сегодня: 1) Запустить меня на станцию <Омега> для проверки. 2) Составить отчет для технического отдела. 3) Составить отчет для шишек выше о готовности продукта.4) Знатно отдохнуть после этого."),
                components=[
                    Button(style=ButtonStyle.blue, label="Продолжить"),
                ]),
        responce = await bot.wait_for("button_click")
        if responce.component.label == "Продолжить":
            await responce.respond(
                embed=discord.Embed(
                    title="Пока я беседовал в мыслях с самим собой, пришел Кир. Парень он малообщительный, перекинулись банальными приветствиями и он покинул кабинет. Немного волнуется. Интересно с чего бы, если большая часть работы проходит мимо него."),
                components=[
                    Button(style=ButtonStyle.blue, label="Продолжить"),
                ]),
        responce = await bot.wait_for("button_click")
        if responce.component.label == "Продолжить":
            await responce.respond(
                embed=discord.Embed(
                    title="Яр- «Утречко, Раст просил передать его сегодня не будет. Чёт херово ему прям очень, чуть ли не в скорою забирают.»"),
                components=[
                    Button(style=ButtonStyle.blue, label="Продолжить"),
                ]),
        responce = await bot.wait_for("button_click")
        if responce.component.label == "Продолжить":
            await responce.respond(
                embed=discord.Embed(
                    title="Пока я был в своих мыслях пришел Яр с крайне печальной новостью. Пусть и справимся мы вдвоем, печально что Раст пропустит свой первый проект. ГГ- «И тебе утро Яр, мы вроде и вдвоем справимся но жалко что Раст это пропустит.»"),
                components=[
                    Button(style=ButtonStyle.blue, label="Продолжить"),
                ]),
        responce = await bot.wait_for("button_click")
        if responce.component.label == "Продолжить":
            await responce.respond(
                embed=discord.Embed(
                    title="Яр-«Хреновенько», сказал Яр почесав за головой, «Впрочем ничего кроме кучи бумажной рутинны он не пропустил, а праздновать всё равно потом с ним будем»."),
                components=[
                    Button(style=ButtonStyle.red, label="Молча кивнуть в знак согласия"),
                    Button(style=ButtonStyle.green, label="Блин, может позвоним ему?Вдруг ему лучше?"),
                ]),
            responce = await bot.wait_for("button_click")
            if responce.component.label == "Молча кивнуть в знак согласия":
                await responce.respond(embed=discord.Embed(
                    title="Яр-«Ну что кєп раньше начнём, раньше закончим»."),
                    components=[
                        Button(style=ButtonStyle.blue, label="Продолжить"),

                    ]),
            if responce.component.label == "Блин, может позвоним ему?Вдруг ему лучше?":
                await responce.respond(embed=discord.Embed(
                    title="Яр-«Кэп у нас не временни, даже если вдруг ему стало лучше мы задержимся на +- час, а так уже часть симуляции будет проведена»"),
                    components=[
                        Button(style=ButtonStyle.blue, label="Продолжить"),
                    ]),
            responce = await bot.wait_for("button_click")
            if responce.component.label == "Продолжить":
                await responce.respond(
                    embed=discord.Embed(
                        title="ГГ-« Итак работаем как обычно, но я иду на два дня вместо одного. Для большей статистики.Ускоренние ставь 19.5x-21x что бы за два часа управились»"),
                    components=[
                        Button(style=ButtonStyle.blue, label="Продолжить"),
                    ]),
            responce = await bot.wait_for("button_click")
            if responce.component.label == "Продолжить":
                await responce.respond(
                    embed=discord.Embed(
                        title="Яр-«Окей кэп, как по бумажке, ты заходишь проводишь там два дня под моим кураторством , после чего выходишь сам или по истечению времени я тебя вывожу»."),
                    components=[
                        Button(style=ButtonStyle.blue, label="Продолжить"),
                    ]),
            responce = await bot.wait_for("button_click")
            if responce.component.label == "Продолжить":
                await responce.respond(
                    embed=discord.Embed(
                        title="Итак я думаю стоит немного рассказать про станцию «Омега». По плану это орбитальный форпост с населением 40-50 тыс. человек. Первоначальная цель проекта наладить инфраструктуру для достаточного снабжения станции."),
                    components=[
                        Button(style=ButtonStyle.blue, label="Продолжить"),
                    ]),
            responce = await bot.wait_for("button_click")
            if responce.component.label == "Продолжить":
                await responce.respond(
                    embed=discord.Embed(
                        title="В будущем станция станет символов выхода человечества в космос\расцветом новой эры, а также главным торговым форпостом в солнечной системе.Главное преимущество Alife что он генерирует и симулирует будущее. "),
                    components=[
                        Button(style=ButtonStyle.blue, label="Продолжить"),
                    ]),

            responce = await bot.wait_for("button_click")
            if responce.component.label == "Продолжить":
                await responce.respond(
                    embed=discord.Embed(
                        title="Т.е. на данный момент такую станцию построить крайне проблематично, а запустить практически не реально. "),
                    components=[
                        Button(style=ButtonStyle.blue, label="Продолжить"),
                    ]),
            responce = await bot.wait_for("button_click")
            if responce.component.label == "Продолжить":
                await responce.respond(
                    embed=discord.Embed(
                        title="Но для ученых понимание, даже приблизительное  как это может функционировать, даст очень большой толчок для создания такого проекта в нашей жизни. Может сначала и уменьшат масштаб до 10 тыс. человек."),
                    components=[
                        Button(style=ButtonStyle.blue, label="Продолжить"),
                    ]),
            responce = await bot.wait_for("button_click")
            if responce.component.label == "Продолжить":
                await responce.respond(
                    embed=discord.Embed(
                        title="Сев в кресло и надевши обруч для подключения на виртуальную станцию «Омега», я дал знак Яру и закрыл глаза.По плану я буду кораблём снабжения с Земли, который привёз необходимые для жизни продукты и вещи"),
                    components=[
                        Button(style=ButtonStyle.blue, label="Продолжить"),
                    ]),
            responce = await bot.wait_for("button_click")
            if responce.component.label == "Продолжить":
                await responce.respond(
                    embed=discord.Embed(
                        title="За день разгружусь,после еще один день проведу в исследовании станции.После сяду на тот же корабль и вернусь на Землю и в реальных мир.Либо если не получится вылететь вечером второго дня,ночью со   второго дня на третий меня принудительно выведет Яр."),
                    components=[
                        Button(style=ButtonStyle.blue, label="Продолжить"),
                    ]),
            responce = await bot.wait_for("button_click")
            if responce.component.label == "Продолжить":
                await responce.respond(
                    embed=discord.Embed(
                        title="Сухо в горле.Сделавши глоток из бутылки которую удачно купил утром я закрыл глаза и сказал-«Начать подключение»"),
                    components=[
                        Button(style=ButtonStyle.blue, label="Продолжить"),
                    ]),
            if responce.component.label == "Продолжить":
                await responce.respond(
                    embed=discord.Embed(
                        title="Сухо в горле.Кх, делать нечего, обману рецепторы водой на станции.«Начать подключение» - спокойно сказал я."),
                    components=[
                        Button(style=ButtonStyle.blue, label="Продолжить"),
                    ]),
            responce = await bot.wait_for("button_click")
            if responce.component.label == "Продолжить":
                await responce.respond(
                    embed=discord.Embed(
                        title="Вдох,Выдох,Вдох,Выдох. Я открыл глаза и оказался в кабине пилота корабля HR-345. Если судить по приборам до станции 20 минут ходу."),
                    components=[
                        Button(style=ButtonStyle.blue, label="Продолжить"),
                    ]),

            responce = await bot.wait_for("button_click")
            if responce.component.label == "Продолжить":
                await responce.respond(
                    embed=discord.Embed(
                        title="До прикосновения с  точкой назначения 5 минут, пора начинать. ГГ-« Станция «Омега» говорит пилот корабля HR-345, запрашиваю разрешения на посадку.»"),
                    components=[
                        Button(style=ButtonStyle.blue, label="Продолжить"),
                    ]),
            responce = await bot.wait_for("button_click")
            if responce.component.label == "Продолжить" and v==1:
                await responce.respond(
                    embed=discord.Embed(
                        title="Диспечер –«Станция «Омега», посадку корабля HR-345 разрешаю, направляйтесь в порт D1. Вам нужна инженерная команда срочного реагирования?»"),
                    components=[
                        Button(style=ButtonStyle.blue, label="Продолжить"),
                    ]),
            responce = await bot.wait_for("button_click")
            if responce.component.label == "Продолжить":
                await responce.respond(
                    embed=discord.Embed(
                        title="ГГ-«Спасибо, корабль в полном порядке. Направляюсь в порт D1, корабль HR-345,конец связи.»"),
                    components=[
                        Button(style=ButtonStyle.blue, label="Продолжить"),
                    ]),
            responce = await bot.wait_for("button_click")
            if responce.component.label == "Продолжить":
                await responce.respond(
                    embed=discord.Embed(
                        title="Приближаюсь к доку, так. Захваты сработали. Уменьшаем тягу до 20%. Дать разрешение на закреплении. Отчёт диспетчеру о стыковке и фух…Я на станции"),
                    components=[
                        Button(style=ButtonStyle.blue, label="Продолжить"),
                    ]),
            responce = await bot.wait_for("button_click")
            if responce.component.label == "Продолжить":
                await responce.respond(
                    embed=discord.Embed(
                        title="Выйдя из корабля я видел такой футуристический, но такой знакомый пейзаж города будущего. Правда из того самого мрачного, где победили корпорации и т.д. , а не счастливый техно-скачек."),
                    components=[
                                   Button(style=ButtonStyle.blue, label="Продолжить"),
                        ]),
            responce = await bot.wait_for("button_click")
            if responce.component.label == "Продолжить":
                await responce.respond(
                    embed=discord.Embed(
                        title="Темная прямо-геометрическая застройка без капельки дизайнерских решений. Благодаря искусственной гравитации, сквозь симуляцию экосферы, а точнее симуляции неба и туч виднелись перевёрнутые дома над головой."),
                    components=[
                        Button(style=ButtonStyle.blue, label="Продолжить"),
                    ]),
            responce = await bot.wait_for("button_click")
            if responce.component.label == "Продолжить":
                await responce.respond(
                    embed=discord.Embed(
                        title="Ну что же, здесь я и проведу следующие два дня."),
                    components=[
                        Button(style=ButtonStyle.blue, label="Продолжить"),
                    ]),
            responce = await bot.wait_for("button_click")
            if responce.component.label == "Продолжить":
                await ctx.send(
                    embed=discord.Embed(title="День первый "),
                    components=[
                        Button(style=ButtonStyle.green, label="Продолжить"),

                    ]
                ),
            responce = await bot.wait_for("button_click")
            if responce.component.label == "Продолжить":
                await responce.respond(embed=discord.Embed(
                    title="Кто бы что не говорил, наблюдать за развитием и стоять своими ногами на космической станции, даже виртуальной , совершенно разные ощущения"),
                                       components=[
                                           Button(style=ButtonStyle.blue, label="Продолжить"),

                                       ]),
            responce = await bot.wait_for("button_click")
            if responce.component.label == "Продолжить":
                await responce.respond(embed=discord.Embed(
                    title="Некоторые люди готовы отдать всё что у них есть, дабы побывать в космосе пару часов, а я сейчас стою посреди космоса и вместо красоты звёзд, вижу мрачные тёмные постройки шпиле-подобного типа"),
                    components=[
                        Button(style=ButtonStyle.blue, label="Продолжить"),

                    ]),
            responce = await bot.wait_for("button_click")
            if responce.component.label == "Продолжить":
                await responce.respond(embed=discord.Embed(
                    title=" Мои размышления прервал докер. Докер- «Как дорога прошла? Космический шлак не сильно помешал?»."),
                    components=[
                        Button(style=ButtonStyle.blue, label="Продолжить"),

                    ]),
            responce = await bot.wait_for("button_click")
            if responce.component.label == "Продолжить":
                await responce.respond(embed=discord.Embed(
                    title=" ГГ-«Кораблям стали ставить улучшенные кинетические щиты. Если что и прилетает, максимум потрясёт немного. Крайне удачная модель.»"),
                    components=[
                        Button(style=ButtonStyle.blue, label="Продолжить"),

                    ]),
            responce = await bot.wait_for("button_click")
            if responce.component.label == "Продолжить":
                await responce.respond(embed=discord.Embed(
                    title="Докер-«Ясно, ну в общем мы корабль разгрузим, можете идти по своим делам. У вас их сейчас должно быть много.»"),
                    components=[
                        Button(style=ButtonStyle.blue, label="Продолжить"),

                    ]),
            responce = await bot.wait_for("button_click")
            if responce.component.label == "Продолжить":
                await responce.respond(embed=discord.Embed(
                    title="Дел у меня было не много, но они были. Итак по плану нужно посетить два места. Первое- центр СБО(служба безопасности Омеги), что бы получить карту личности. Удостоверение без которого не выйдет ничего на станции."),
                    components=[
                        Button(style=ButtonStyle.blue, label="Продолжить"),

                    ]),
            responce = await bot.wait_for("button_click")
            if responce.component.label == "Продолжить":
                await responce.respond(embed=discord.Embed(
                    title="В зависимости от человека и его рода деятельности карта получает разный уровень доступа. Мой будет как у обычного гражданского на станции, но с упоминанием что я не местный если потребуется проверка."),
                    components=[
                        Button(style=ButtonStyle.blue, label="Продолжить"),

                    ]),
            responce = await bot.wait_for("button_click")
            if responce.component.label == "Продолжить":
                await responce.respond(embed=discord.Embed(
                    title="После нужно зайти в административный центр. Передать данные о грузе и получить место жительства на время пребывания на станции, а также возможно узнать новости. За почти год многое могло измениться."),
                    components=[
                        Button(style=ButtonStyle.blue, label="Продолжить"),

                    ]),
            responce = await bot.wait_for("button_click")
            if responce.component.label == "Продолжить":
                await responce.respond(embed=discord.Embed(
                    title="9)Зайдя в лифт в доках предо мной стал выбор.1)Этаж -12 «Академия СБО.2)Этаж 5 Центр оказания административных услуг"),
                    components=[
                        Button(style=ButtonStyle.green, label="Этаж -12"),
                        Button(style=ButtonStyle.red, label="Этаж 5"),

                    ]),
            responce = await bot.wait_for("button_click")
            if responce.component.label == "Этаж -12":
                s=s+1
                await responce.respond(embed=discord.Embed(
                    title="СБО-Наверно первый делом стоит получить карту, а потом уже узнавать куда идти отдыхать. Всё равно без карты я туда не попаду"),
                                       components=[
                                           Button(style=ButtonStyle.blue, label="Продолжить"),

                                       ]),
            if responce.component.label == "Этаж 5":
                await responce.respond(embed=discord.Embed(
                    title="Админ центр-логично сначала заявить что я прибыл и с чем, а потом получать карту для прохода по станции"),
                                       components=[
                                           Button(style=ButtonStyle.blue, label="Далее"),

                                       ]),
            responce = await bot.wait_for("button_click")
            if responce.component.label == "Продолжить":
                await responce.respond(embed=discord.Embed(
                    title="Зайдя в лифт нажал на этаж -12 «Академия СБО» .Одно из главных преимуществ станции, крайне продуманная вертикальная инфраструктура. Места не так много, а потолок тоже пол если правильно посмотреть"),
                    components=[
                        Button(style=ButtonStyle.blue, label="Продолжить"),

                    ]),
            if responce.component.label == "Далее":
                await responce.respond(embed=discord.Embed(
                    title="Зайдя в лифт я нажал на 5 этаж. Одно из главных преимуществ станции, крайне продуманная вертикальная инфраструктура. Места не так много, а потолок тоже пол если правильно посмотреть."),
                    components=[
                        Button(style=ButtonStyle.blue, label="Далее"),

                    ]),
            responce = await bot.wait_for("button_click")
            if responce.component.label == "Продолжить":
                await responce.respond(embed=discord.Embed(
                    title="Спустившись, я увидел огромный атриум и один столик у которого сотрудник СБО что-то обговаривал с местным. Прервал их беседу и узнал куда мне нужно. Сотрудник показал рукой на дверь справа."),
                    components=[
                        Button(style=ButtonStyle.blue, label="Продолжить"),

                    ]),
            if responce.component.label == "Далее":
                await responce.respond(embed=discord.Embed(
                    title="Выйдя из лифта я обнаружил коридор, дверь и ресепшн около неё. Подойдя к двери мужчина за стойкой не обратил на меня никакого внимания, так что я окликнул его"),
                    components=[
                        Button(style=ButtonStyle.blue, label="Далее"),

                    ]),
            responce = await bot.wait_for("button_click")
            if responce.component.label == "Продолжить":
                await responce.respond(embed=discord.Embed(
                    title="Кивнув в знак благодарности зашел в дверь. Внутри мужчина в форме строителя-инженера говорил с дамой за стойкой. Присев на диван ожидания решил послушать их разговор."),
                    components=[
                        Button(style=ButtonStyle.blue, label="Продолжить"),

                    ]),
            if responce.component.label == "Далее":
                await responce.respond(embed=discord.Embed(
                    title="ГГ-«Добрый день. Я торговец прибыл сегодня и мне нужно передать информацию о грузе и получить место жительства.»"),
                    components=[
                        Button(style=ButtonStyle.blue, label="Далее"),

                    ]),

            responce = await bot.wait_for("button_click")
            if responce.component.label == "Продолжить":
                await responce.respond(embed=discord.Embed(
                    title="Тех.сотрудник-« Я всё понимаю, ограничения и так далее,но у нас ведущий инженер получил ранение,а завал в зоне H-32 сам себя разбирать не будет,так что с разрешением начальства повысьте мой технический доступ»."),
                    components=[
                        Button(style=ButtonStyle.blue, label="Продолжить"),

                    ]),
            if responce.component.label == "Далее":
                await responce.respond(embed=discord.Embed(
                    title="Секретарь поднял на меня глаза и сказал-«Хорошо, направо и до конца, кабинет слева ваш». Дверь открылась."),
                    components=[
                        Button(style=ButtonStyle.blue, label="Далее"),

                    ]),
            responce = await bot.wait_for("button_click")
            if responce.component.label == "Продолжить":
                await responce.respond(embed=discord.Embed(
                    title="Сотрудница СБО-«Боже, я не могу просто дать вам доступ выше. Мне нужно назначить за вами ответственного который спустя время восстановления вашего старшего заберёт у вас этот доступ»."),
                    components=[
                        Button(style=ButtonStyle.blue, label="Продолжить"),

                    ]),
            if responce.component.label == "Далее":
                await responce.respond(embed=discord.Embed(
                    title="Внутри меня ждала куча кабинетов, найдя нужный мне с табличкой «Центр помощи гражданам» постучал и зашел внутрь. Внутри меня ждал один стол и мужчина преклонного возраста. "),
                    components=[
                        Button(style=ButtonStyle.blue, label="Далее"),

                    ]),
            responce = await bot.wait_for("button_click")
            if responce.component.label == "Продолжить":
                await responce.respond(embed=discord.Embed(
                    title="Сотрудница СБО-«Я подала заявку её рассмотрят и примут в течении 2-3 часов. Пожалуйста подождите это время.»"),
                    components=[
                        Button(style=ButtonStyle.blue, label="Продолжить"),

                    ]),
            if responce.component.label == "Далее":
                await responce.respond(embed=discord.Embed(
                    title="ГГ-«Здравствуйте, я торговец. Только сегодня прибыл. Пришел к вам передать информацию о грузе на борту и получить место жительства». Сказал я и передал ему накопитель."),
                    components=[
                        Button(style=ButtonStyle.blue, label="Далее"),

                    ]),
            responce = await bot.wait_for("button_click")
            if responce.component.label == "Продолжить":
                await responce.respond(embed=discord.Embed(
                    title="Тех.сотрудник-«И на этом спасибо. Всего доброго»"),
                    components=[
                        Button(style=ButtonStyle.blue, label="Продолжить"),

                    ]),
            if responce.component.label == "Далее":
                await responce.respond(embed=discord.Embed(
                    title="Оператор-«Хорошо, молодой человек. Заполните анкету, а я пока считаю ваш груз». И передал мне терминал для заполнения."),
                    components=[
                        Button(style=ButtonStyle.blue, label="Далее"),

                    ]),
            responce = await bot.wait_for("button_click")
            if responce.component.label == "Продолжить":
                await responce.respond(embed=discord.Embed(
                    title="Хм, завал в зоне, значит недавно случилась авария или несчастный случай, нужно будет узнать подробней об этом в административном центре. Подумал я направляясь к стойке."),
                    components=[
                        Button(style=ButtonStyle.blue, label="Продолжить"),

                    ]),
            if responce.component.label == "Далее":
                await responce.respond(embed=discord.Embed(
                    title="Заполнил терминал и передал оператору. В процессе забрал свой личный накопитель"),
                    components=[
                        Button(style=ButtonStyle.blue, label="Далее"),

                    ]),
            responce = await bot.wait_for("button_click")
            if responce.component.label == "Продолжить":
                await responce.respond(embed=discord.Embed(
                    title="Сотрудница СБО-«Да, мужчина. Я вас слушаю» ГГ-«Я торговец, прибыл сегодня на корабле HR-345, должен получить карту на время пребывания на станции.»."),
                    components=[
                        Button(style=ButtonStyle.blue, label="Продолжить"),

                    ]),
            if responce.component.label == "Далее":
                await responce.respond(embed=discord.Embed(
                    title="Оператор-«Ваша квартира в секторе H-31. Когда вы получите карту квартиру уже будет подвязана к ней. Подробное местонахождение сможете узнать из терминала помощи.»"),
                    components=[
                        Button(style=ButtonStyle.blue, label="Далее"),

                    ]),
            responce = await bot.wait_for("button_click")
            if responce.component.label == "Продолжить":
                await responce.respond(embed=discord.Embed(
                    title="Сотрудница СБО-«Информация о вас есть, хорошо. Сейчас вернусь». Сотрудница развернулась на кресле и достала из шкафа универсальную карту. После провела ею под облучателем и вручила мне."),
                    components=[
                        Button(style=ButtonStyle.blue, label="Продолжить"),

                    ]),
            if responce.component.label == "Далее":
                await responce.respond(embed=discord.Embed(
                    title="Оператор-«В академии не спорьте если у вас заберут доступ в некоторые сектора. После последних происшествий в связи с нарушением техники безопасности власти стали ограничивать доступ.»"),
                    components=[
                        Button(style=ButtonStyle.blue, label="Далее"),

                    ]),
            responce = await bot.wait_for("button_click")
            if responce.component.label == "Продолжить":
                await responce.respond(embed=discord.Embed(
                    title="ГГ-«Благодарю, хорошего дня». Пожелал я и направился в админ центр. Снова зайдя в лифт я выбрал 5 этаж."),
                    components=[
                        Button(style=ButtonStyle.blue, label="Продолжить"),

                    ]),
            if responce.component.label == "Далее":
                await responce.respond(embed=discord.Embed(
                    title="Хм, интересно каковы последствия «нарушения техники безопасности». Я поблагодарил оператора за совет и вскоре покинул кабинет. Оказавшись в лифте я выбрал этаж -12 «Академия СБО»."),
                    components=[
                        Button(style=ButtonStyle.blue, label="Далее"),

                    ]),
            responce = await bot.wait_for("button_click")
            if responce.component.label == "Продолжить":
                await responce.respond(embed=discord.Embed(
                    title="Выйдя из лифта я обнаружил коридор, дверь и ресепшн около неё. Подойдя к двери мужчина за стойкой не обратил на меня никакого внимания, так что я провёл карточкой и зашел внутрь."),
                    components=[
                        Button(style=ButtonStyle.blue, label="Продолжить"),

                    ]),
            if responce.component.label == "Далее":
                await responce.respond(embed=discord.Embed(
                    title="Спустившись, я увидел огромный атриум и один столик у которого сотрудник СБО что то попивал из кружки. Узнал от него куда мне нужно. Сотрудник показал рукой на дверь справа."),
                    components=[
                        Button(style=ButtonStyle.blue, label="Далее"),

                    ]),
            responce = await bot.wait_for("button_click")
            if responce.component.label == "Продолжить":
                await responce.respond(embed=discord.Embed(
                    title="Внутри меня ждала куча кабинетов, найдя на одной из дверей табличку «Центр помощи гражданам» постучал и зашел внутрь. Внутри меня ждал один стол и мужчина преклонного возраста. "),
                    components=[
                        Button(style=ButtonStyle.blue, label="Продолжить"),

                    ]),
            if responce.component.label == "Далее":
                await responce.respond(embed=discord.Embed(
                    title="Кивнув в знак благодарности зашел в дверь. Внутри была дама за стойкой. ГГ-«Я торговец, прибыл сегодня на корабле HR-345, должен получить карту на время пребывания на станции.»"),
                    components=[
                        Button(style=ButtonStyle.blue, label="Далее"),

                    ]),
            responce = await bot.wait_for("button_click")
            if responce.component.label == "Продолжить":
                await responce.respond(embed=discord.Embed(
                    title="ГГ-«Здравствуйте, я торговец. Только сегодня прибыл. Уже получил карту. Пришел к вам передать информацию о грузе на порту и получить место жительства». Сказал я и передал ему накопитель."),
                    components=[
                        Button(style=ButtonStyle.blue, label="Продолжить"),

                    ]),
            if responce.component.label == "Далее":
                await responce.respond(embed=discord.Embed(
                    title="Сотрудница СБО-«Информация о вас есть, хорошо. Сейчас вернусь». Сотрудница развернулась на кресле и достала из шкафа универсальную карту. После провела ею под облучателем и вручила мне."),
                    components=[
                        Button(style=ButtonStyle.blue, label="Далее"),

                    ]),
            responce = await bot.wait_for("button_click")
            if responce.component.label == "Продолжить":
                await responce.respond(embed=discord.Embed(
                    title="Оператор-«Хорошо, молодой человек. Проведите пожалуйста картой здесь, а я пока считаю ваш груз». И указал рукой на сканер."),
                    components=[
                        Button(style=ButtonStyle.blue, label="Продолжить"),

                    ]),
            if responce.component.label == "Далее":
                await responce.respond(embed=discord.Embed(
                    title="Сотрудница СБО –«За вашей картой уже прикреплён дом в секторе H-31. К сожалению по техническим причинам доступ в сектор H-32 ограничен. Прошу отнестись с пониманием.» "),
                    components=[
                        Button(style=ButtonStyle.blue, label="Далее"),

                    ]),
            responce = await bot.wait_for("button_click")
            if responce.component.label == "Продолжить":
                await responce.respond(embed=discord.Embed(
                    title="Оператор-«Ваша квартира в секторе H-31. Подробно  сможете узнать из терминала помощи».Проведя картой и забрав личный накопитель, я поблагодарил оператора и вскоре покинул кабинет."),
                    components=[
                        Button(style=ButtonStyle.blue, label="Продолжить"),

                    ]),
            if responce.component.label == "Далее":
                await responce.respond(embed=discord.Embed(
                    title="ГГ-«Благодарю, хорошего дня». Пожелал я и направился к лифту. "),
                    components=[
                        Button(style=ButtonStyle.blue, label="Продолжить"),

                    ]),

            responce = await bot.wait_for("button_click")
            if responce.component.label == "Продолжить":
                await responce.respond(embed=discord.Embed(
                    title="Снова оказавшись в лифте я выбрал 0 этаж «Ангар». Там арендую аэрокар и отправлюсь к дому"),
                    components=[
                        Button(style=ButtonStyle.blue, label="Продолжить"),

                    ]),
            responce = await bot.wait_for("button_click")
            if responce.component.label == "Продолжить":
                await responce.respond(embed=discord.Embed(
                    title="Ангар выглядел как огромный прямоугольник без одной грани. Сам зал делился на подобие 2 этажей с закрепленными с помощью захватов аэрокарами. Вся инфраструктура станции это лифты и аэрокары."),
                    components=[
                        Button(style=ButtonStyle.blue, label="Продолжить"),

                    ]),
            responce = await bot.wait_for("button_click")
            if responce.component.label == "Продолжить":
                await responce.respond(embed=discord.Embed(
                    title="Сами аэрокары работают на технологии эффекта массы. Предполагаемый нулевой элемент под воздействием электрического тока способен увеличивать или уменьшать массу единицы объема пространства-времени."),
                    components=[
                        Button(style=ButtonStyle.blue, label="Продолжить"),

                    ]),
            responce = await bot.wait_for("button_click")
            if responce.component.label == "Продолжить":
                await responce.respond(embed=discord.Embed(
                    title="Если подано положительное напряжение, масса увеличивается, если отрицательное — уменьшается. Чем сила тока больше, тем больше энергия поля эффекта массы"),
                    components=[
                        Button(style=ButtonStyle.blue, label="Продолжить"),

                    ]),
            responce = await bot.wait_for("button_click")
            if responce.component.label == "Продолжить":
                await responce.respond(embed=discord.Embed(
                    title="Поля, снижающие массу, используются для перемещений на сверхсветовых скоростях. Поля, увеличивающие массу, позволяют создавать искусственную гравитацию и защищают корабли от различных обломков в космосе."),
                    components=[
                        Button(style=ButtonStyle.blue, label="Продолжить"),

                    ]),
            responce = await bot.wait_for("button_click")
            if responce.component.label == "Продолжить":
                await responce.respond(embed=discord.Embed(
                    title="Сев в свободный кар, провёл картой и указал пункт назначения «сектор H-31». Для избежания аварий, которые в условиях станции создадут огромную опасность для всего населения сектора, кары используют автопилот."),
                    components=[
                        Button(style=ButtonStyle.blue, label="Продолжить"),

                    ]),
            responce = await bot.wait_for("button_click")
            if responce.component.label == "Продолжить":
                await responce.respond(embed=discord.Embed(
                    title="Меня ждала поездка или правильней сказать полёт с видом на промышленные сектора от сектора A до F, а потом пролёт через коммерческий центр G. В целом это займёт минут 10 по данным автопилота."),
                    components=[
                        Button(style=ButtonStyle.blue, label="Продолжить"),

                    ]),
            responce = await bot.wait_for("button_click")
            if responce.component.label == "Продолжить":
                await responce.respond(embed=discord.Embed(
                    title="Опустившись на местной площадке для каров, я покинул автомобиль и подошел к терминалу помощи,он стоял прям на выходе из места приземления. "),
                    components=[
                        Button(style=ButtonStyle.blue, label="Продолжить"),

                    ]),
            responce = await bot.wait_for("button_click")
            if responce.component.label == "Продолжить":
                await responce.respond(embed=discord.Embed(
                    title="Терминалы представляли собой аналог википедии  по станции. На нём можно было посмотреть план всей станции. В какие сектора имеется доступ с моей картой. Узнать ближайший путь к чему угодно."),
                    components=[
                        Button(style=ButtonStyle.blue, label="Продолжить"),

                    ]),
            responce = await bot.wait_for("button_click")
            if responce.component.label == "Продолжить":
                await responce.respond(embed=discord.Embed(
                    title="Просмотреть новости станции, узнать о планируемых мероприятиях для местных ,посмотреть цены. В общем универсальный помощник во всём."),
                    components=[
                        Button(style=ButtonStyle.blue, label="Продолжить"),

                    ]),
            responce = await bot.wait_for("button_click")
            if responce.component.label == "Продолжить":
                await responce.respond(embed=discord.Embed(
                    title="Посмотрев путь к дому, я также узнал что в моем секторе есть кафе-бар и ресторан средне-высокого класса. Отсутствие банального супермаркета удручало, но таково построение станции."),
                    components=[
                        Button(style=ButtonStyle.blue, label="Продолжить"),

                    ]),
            responce = await bot.wait_for("button_click")
            if responce.component.label == "Продолжить":
                await responce.respond(embed=discord.Embed(
                    title="Ресторан меня особо не интересовал, а вот в бар можно было заглянуть и заодно попробовать узнать  про аварию в соседнем секторе. "),
                    components=[
                        Button(style=ButtonStyle.blue, label="Продолжить"),

                    ]),
            responce = await bot.wait_for("button_click")
            if responce.component.label == "Продолжить":
                await responce.respond(embed=discord.Embed(
                    title="Дойдя до дома зашел в него, а после и в квартиру с помощью карты. Внутри меня ждала обычная квартира Classic. На станции квартиры делились на 4 уровня."),
                    components=[
                        Button(style=ButtonStyle.blue, label="Продолжить"),

                    ]),
            responce = await bot.wait_for("button_click")
            if responce.component.label == "Продолжить":
                await responce.respond(embed=discord.Embed(
                    title="Low-квартира для одиноких людей или стариков которые остались одни. Classic – как у меня, рассчитана на семью с одним ребенком. Classic-high- для семей с  двумя или тремя детьми."),
                    components=[
                        Button(style=ButtonStyle.blue, label="Продолжить"),

                    ]),
            responce = await bot.wait_for("button_click")
            if responce.component.label == "Продолжить":
                await responce.respond(embed=discord.Embed(
                    title="На станции строго запрещено иметь больше трёх детей. И Premium- для ввысшего класса. На станции не обещали равную жизнь для всех. Все будут жить достойно но не равно. Таков он-капитализм. "),
                    components=[
                        Button(style=ButtonStyle.blue, label="Продолжить"),

                    ]),
            responce = await bot.wait_for("button_click")
            if responce.component.label == "Продолжить":
                await responce.respond(embed=discord.Embed(
                    title="Прибыл на станцию я к обеду, а сейчас время идёт к вечеру. Не мешало бы перекусить. На выбор у меня есть 2 способа провести вечер."),
                    components=[
                        Button(style=ButtonStyle.green, label="Кафе-бар"),
                        Button(style=ButtonStyle.red, label="Ресторан"),
                    ]),
            responce = await bot.wait_for("button_click")
            if responce.component.label == "Кафе-бар":
                b=b+1
                await responce.respond(embed=discord.Embed(
                    title="Я решил пойти в бар. Возможностей разузнать про аварию там больше, да и кухня для богатеньких меня особо не интересовала."),
                    components=[
                        Button(style=ButtonStyle.blue, label="Продолжить"),

                    ]),
            if responce.component.label == "Ресторан":
                await responce.respond(embed=discord.Embed(
                    title="Всё таки мне завтра лететь обратно, а делать это с похмелья крайне неприятно. Да и я хочу поесть вкусно, а не выпить."),
                    components=[
                        Button(style=ButtonStyle.blue, label="Далее"),

                    ]),
            responce = await bot.wait_for("button_click")
            if responce.component.label == "Продолжить":
                await responce.respond(embed=discord.Embed(
                    title="Зайдя в зал увидел типичный земной бар. Зал был на половину пустой, а около стойки бармен разговаривал с одним из клиентов. Решил попробовать подсесть к ним."),
                    components=[
                        Button(style=ButtonStyle.blue, label="Продолжить"),

                    ]),
            if responce.component.label == "Далее":
                await responce.respond(embed=discord.Embed(
                    title="Внутри ресторана меня ждал огромный зал и мебель из дерева. Удивительно, привезти сюда мебель из дерева достаточно дорого. На удивление зал был забит почти полностью."),
                    components=[
                        Button(style=ButtonStyle.blue, label="Далее"),

                    ]),
            responce = await bot.wait_for("button_click")
            if responce.component.label == "Продолжить":
                await responce.respond(embed=discord.Embed(
                    title="ГГ-«Вечерок вашему дуэту, не против моей компании? Только в обед прибыл, завтра вечером уже отбывать. Хочется отдохнуть сегодня знатно."),
                    components=[
                        Button(style=ButtonStyle.blue, label="Продолжить"),

                    ]),
            if responce.component.label == "Далее":
                await responce.respond(embed=discord.Embed(
                    title="Среди занятых мест мне удалось увидеть свободный столик, сев за который мне спроецировалась голограмма меню.Преимуществом ресторана были повара из разных культурных групп. "),
                    components=[
                        Button(style=ButtonStyle.blue, label="Далее"),

                    ]),
            responce = await bot.wait_for("button_click")
            if responce.component.label == "Продолжить":
                await responce.respond(embed=discord.Embed(
                    title="Бармен-«Садись рядом, интересно что там нового на Земле-то»"),
                    components=[
                        Button(style=ButtonStyle.blue, label="Продолжить"),

                    ]),
            if responce.component.label == "Далее":
                await responce.respond(embed=discord.Embed(
                    title="То есть меню представляет собой блюда со всего шарика в одном месте. Долго выбирая в меню я остановил свой выбор на говяжьем брискете из Техаса, аналог стейка но максимально нежный."),
                    components=[
                        Button(style=ButtonStyle.blue, label="Далее"),

                    ]),
            responce = await bot.wait_for("button_click")
            if responce.component.label == "Продолжить":
                await responce.respond(embed=discord.Embed(
                    title="В ходе разговора узнал что бармена звали  Мордин, а его собеседника Явик. Разговор шёл достаточно бодро и местная выпивка этому способствовала. Спустя определённое время я всё-таки решил спросить."),
                    components=[
                        Button(style=ButtonStyle.blue, label="Продолжить"),

                    ]),
            if responce.component.label == "Далее":
                await responce.respond(embed=discord.Embed(
                    title="И дим-самы из Гонконга на закуску, подобие пельменей но не с мясной начинкой. Выбрав что я хочу, меню проинформировало меня о времени ожидания «15-20 минут до первого блюда»."),
                    components=[
                        Button(style=ButtonStyle.blue, label="Далее"),

                    ]),
            responce = await bot.wait_for("button_click")
            if responce.component.label == "Продолжить":
                await responce.respond(embed=discord.Embed(
                    title="ГГ-«Слышали про аварию в секторе H-32, что там могло случится,что аж закрыли гражданский сектор. Это ж надо перераспределить целый сектор заново. Сколько я летаю,а такого не помню.»"),
                    components=[
                        Button(style=ButtonStyle.blue, label="Продолжить"),

                    ]),
            if responce.component.label == "Далее":
                await responce.respond(embed=discord.Embed(
                    title="Пока ждал заказ воспользовался блоком данных лежащим рядом и посмотрел новости. Из интересного было недавнее смещение главы СБО. Надобно думать после того самого происшествия."),
                    components=[
                        Button(style=ButtonStyle.blue, label="Далее"),

                    ]),
            responce = await bot.wait_for("button_click")
            if responce.component.label == "Продолжить":
                await responce.respond(embed=discord.Embed(
                    title="Явик-« Правительство держит в секрете ,что там случилось но говорят там была лаборатория по исследованию космических объектов и будто бы в процессе исследования камня из космоса там нашли что-то.»"),
                    components=[
                        Button(style=ButtonStyle.blue, label="Продолжить"),

                    ]),
            if responce.component.label == "Далее":
                await responce.respond(embed=discord.Embed(
                    title="Также любая информация о закрытии сектора в открытом доступе отсутствовала. Были некоторые обсуждения с предположениями граждан, но всё просматривается властями и фильтруется."),
                    components=[
                        Button(style=ButtonStyle.blue, label="Далее"),

                    ]),
            responce = await bot.wait_for("button_click")
            if responce.component.label == "Продолжить":
                await responce.respond(embed=discord.Embed(
                    title="Мордин-«И ты в это веришь? Еще бы рассказал что там пришельцы захватили корпус и строят армию. Тьфу. Я скорее верю в неудачную аварию каров из-за чего там очень большие завалы.»"),
                    components=[
                        Button(style=ButtonStyle.blue, label="Продолжить"),

                    ]),
            if responce.component.label == "Далее":
                await responce.respond(embed=discord.Embed(
                    title="Правды или хотя бы предположений в открытых источниках я не найду. Ясно одно, это не просто авария или несчастный случай. Это что то новое, а что?Не мешало бы узнать."),
                    components=[
                        Button(style=ButtonStyle.blue, label="Далее"),

                    ]),
            responce = await bot.wait_for("button_click")
            if responce.component.label == "Продолжить":
                await responce.respond(embed=discord.Embed(
                    title="ГГ-«Ладно ребят, время ближе к полуночи. Классно посидели, но мне пора, а то завтра не вылечу ,а выплыву.»"),
                    components=[
                        Button(style=ButtonStyle.blue, label="Продолжить"),

                    ]),
            if responce.component.label == "Далее":
                await responce.respond(embed=discord.Embed(
                    title="Пока я размышлял мне принесли сразу оба блюда и я был приятно удивлён вкусом этих шедевров кулинарии. Никогда не поверил бы что буду наслаждаться пельменями в элитном ресторана."),
                    components=[
                        Button(style=ButtonStyle.blue, label="Далее"),

                    ]),
            responce = await bot.wait_for("button_click")
            if responce.component.label == "Продолжить":
                await responce.respond(embed=discord.Embed(
                    title="Я попрощался с парнями и пошёл к себе отсыпаться. По пути думал: «Почему Alife решил скрыть причину и последствия аварии?». Он конечно сам решает что ему нужно, но раньше он так не делал."),
                    components=[
                        Button(style=ButtonStyle.blue, label="Продолжить"),

                    ]),
            if responce.component.label == "Далее":
                await responce.respond(embed=discord.Embed(
                    title="Вкусно поужинав, расплатился и отправился домой отдохнуть.  По пути думал: «Почему Alife решил скрыть причину и последствия аварии?». Значит случилось что то новое и AI проверяет способы борьбы с этим новым."),
                    components=[
                        Button(style=ButtonStyle.blue, label="Далее"),

                    ]),
            responce = await bot.wait_for("button_click")
            if responce.component.label == "Продолжить":
                await responce.respond(embed=discord.Embed(
                    title="Значит случилось что-то новое и AI проверяет способы борьбы с этим новым,при этом не создавая паники среди населения.Правда в реале это не сработает. Чем меньше информации-тем больше паника. "),
                    components=[
                        Button(style=ButtonStyle.blue, label="Продолжить"),

                    ]),
            if responce.component.label == "Далее":
                await responce.respond(embed=discord.Embed(
                    title="При этом не создавая паники среди населения.Правда в реале это не сработает.Чем меньше информации тем больше паника."),
                    components=[
                        Button(style=ButtonStyle.blue, label="Далее"),

                    ]),
            responce = await bot.wait_for("button_click")
            if responce.component.label == "Продолжить":
                await responce.respond(embed=discord.Embed(
                    title="Таки дойдя до квартиры быстро скинул с себя одежду и упал в кровать."),
                    components=[
                        Button(style=ButtonStyle.blue, label="Продолжить"),

                    ]),
            if responce.component.label == "Далее":
                await responce.respond(embed=discord.Embed(
                    title="Таки дойдя до квартиры быстро скинул с себя одежду и упал в кровать."),
                    components=[
                        Button(style=ButtonStyle.blue, label="Продолжить"),

                    ]),
            responce = await bot.wait_for("button_click")
            if responce.component.label == "Продолжить":
                await responce.respond(embed=discord.Embed(
                    title="День второй"),
                    components=[
                        Button(style=ButtonStyle.blue, label="Продолжить"),

                    ]),
            responce = await bot.wait_for("button_click")
            if responce.component.label == "Продолжить":
                await responce.respond(
                    embed=discord.Embed(
                        title="Около 8 утра искусственная  имитация солнечного света заставила меня проснутся."),
                    components=[
                        Button(style=ButtonStyle.green, label="Продолжить"),
                    ]
                )
            responce = await bot.wait_for("button_click")
            if responce.component.label == "Продолжить":
                await responce.respond(
                    embed=discord.Embed(
                        title="Сев на кровати и протерев глаза, было принято решение составить план на сегодня. Прибыл на станцию я в +- 16:00,а значит сегодня в это же время мне нужно отбыть или меня выведет Яр."),
                    components=[
                        Button(style=ButtonStyle.blue, label="Продолжить"),

                    ]),
            responce = await bot.wait_for("button_click")
            if responce.component.label == "Продолжить":
                await responce.respond(
                    embed=discord.Embed(
                        title="В принципе весь день свободен. Бюрократия закончилась вчера, но я все еще очень хочу узнать,что случилось в секторе H-32. Желательно увидеть своими глазами эту «аварию»."),
                    components=[
                        Button(style=ButtonStyle.blue, label="Продолжить"),

                    ]),
            responce = await bot.wait_for("button_click")
            if responce.component.label == "Продолжить":
                await responce.respond(
                    embed=discord.Embed(
                        title="Прикинул как я могу это сделать в голове нарисовался мини-план. Немного отполировать во время завтрака и пойдёт.  "),
                    components=[
                        Button(style=ButtonStyle.blue, label="Продолжить"),

                    ]),
            responce = await bot.wait_for("button_click")
            if responce.component.label == "Продолжить":
                await responce.respond(
                    embed=discord.Embed(
                        title="Позавтракать я решил в кафе-баре, барное меню у них только после 20:00. До этого времени бар-это обычное кафе для перекуса на время обеда. Быстро одевшись, закрыл квартиру и отправился в кафе."),
                    components=[
                        Button(style=ButtonStyle.blue, label="Продолжить"),

                    ]),
            responce = await bot.wait_for("button_click")
            if responce.component.label == "Продолжить":
                await responce.respond(
                    embed=discord.Embed(
                        title="Выглядел я не приметно: рубашка, джинсы и кроссы. Типичный житель нашего времени, хотя и здесь это тоже не стало экзотикой. Подходя к кафе,заметил отсутствие красивой неоновой вывески."),
                    components=[
                        Button(style=ButtonStyle.blue, label="Продолжить"),

                    ]),
            responce = await bot.wait_for("button_click")
            if responce.component.label == "Продолжить" and b == 1:
                await responce.respond(embed=discord.Embed(
                    title="Зашел в бар и не увидел знакомого бармена, впрочем может оно и к лучшему. Заказав омлет из двух яиц и жаренный сыр, я принялся дорисовывать план."),
                    components=[
                        Button(style=ButtonStyle.blue, label="Продолжить"),

                    ]),
            if responce.component.label == "Продолжить":
                await responce.respond(embed=discord.Embed(
                    title="Зашел в бар и увидел достаточно красивую (официантку?) за стойкой. Заказав у неё омлет из двух яиц и жаренный сыр, я принялся дорисовывать план."),
                    components=[
                        Button(style=ButtonStyle.blue, label="Продолжить"),

                    ]),
            responce = await bot.wait_for("button_click")
            if responce.component.label == "Продолжить":
                await responce.respond(
                    embed=discord.Embed(
                        title="Итак, разделение между секторами образное, никаких заборов там нету. Ближе всего будет ситуация с Кореей в нашем мире. Люди в Южной Корее делают один шаг и оказываются в Северной."),
                    components=[
                        Button(style=ButtonStyle.blue, label="Продолжить"),

                    ]),
            responce = await bot.wait_for("button_click")
            if responce.component.label == "Продолжить":
                await responce.respond(
                    embed=discord.Embed(
                        title="Так и с секторами. Разделение плановое для большей удобности застройки. Проблем проникнуть в сектор не возникнет. Я уверен,что патрулей там не будет. Проблема потом- «Куда идти?»."),
                    components=[
                        Button(style=ButtonStyle.blue, label="Продолжить"),

                    ]),
            responce = await bot.wait_for("button_click")
            if responce.component.label == "Продолжить":
                await responce.respond(
                    embed=discord.Embed(
                        title="Сектор достаточно большой и тупо ходить по нему не выйдет. Нужно узнать куда идти. Первостепенная задача есть. Если я буду знать куда идти-попасть туда не проблема. "),
                    components=[
                        Button(style=ButtonStyle.blue, label="Продолжить"),

                    ]),
            responce = await bot.wait_for("button_click")
            if responce.component.label == "Продолжить":
                await responce.respond(
                    embed=discord.Embed(
                        title="Вкусно позавтракав и расплатившись, я пошёл на «границу» секторов. Может получится узнать что-то заранее."),
                    components=[
                        Button(style=ButtonStyle.blue, label="Продолжить"),

                    ]),
            responce = await bot.wait_for("button_click")
            if responce.component.label == "Продолжить" and s == 1:
                await responce.respond(embed=discord.Embed(
                    title="Подойдя к сектору, я увидел человека в строительной форме и узнал в нём того самого инженера, который требовал повысить уровень доступа его карты. В принципе,он мог бы мне помочь."),
                    components=[
                        Button(style=ButtonStyle.blue, label="Продолжить"),

                    ]),
            if responce.component.label == "Продолжить":
                await responce.respond(embed=discord.Embed(
                    title="Подойдя к сектору я увидел незнакомого человека в строительной форме. Судя по всему он один из тех кто решает эту «проблемку»"),
                    components=[
                        Button(style=ButtonStyle.blue, label="Далее"),

                    ]),
            responce = await bot.wait_for("button_click")
            if responce.component.label == "Продолжить":
                await responce.respond(embed=discord.Embed(
                    title="Я подошел к нему и поздоровался-«Доброе утро, если я правильно помню,это вы вчера просили повышенный доступ для вашей карты? Я ждал сзади, мне нужна была временная карта.»"),
                    components=[
                        Button(style=ButtonStyle.blue, label="Продолжить"),

                    ]),
            if responce.component.label == "Далее":
                await responce.respond(embed=discord.Embed(
                    title="Я решил осмотреться и прошел по границе сектора. Ничего интересного я там не увидел, но сделать это нужно было."),
                    components=[
                        Button(style=ButtonStyle.blue, label="Далее"),

                    ]),
            responce = await bot.wait_for("button_click")
            if responce.component.label == "Продолжить":
                await responce.respond(embed=discord.Embed(
                    title="Тех.сотрудник-«Доброе, доброе, вы правильно предположили. Действительно я просил повысить мне доступ вчера. Вам что-то нужно?»"),
                    components=[
                        Button(style=ButtonStyle.blue, label="Продолжить"),

                    ]),
            if responce.component.label == "Далее":
                await responce.respond(embed=discord.Embed(
                    title="Мне нужна точка обзора с которой я мог бы видеть весь сектор, а получить её достаточно сложно."),
                    components=[
                        Button(style=ButtonStyle.blue, label="Далее"),

                    ]),
            responce = await bot.wait_for("button_click")
            if responce.component.label == "Продолжить":
                await responce.respond(embed=discord.Embed(
                    title="ГГ-«В общем-то нет, захотелось узнать,получили ли вы карту? Вы сильно настаивали на её необходимости для вас.»"),
                    components=[
                        Button(style=ButtonStyle.blue, label="Продолжить"),

                    ]),
            if responce.component.label == "Далее":
                await responce.respond(embed=discord.Embed(
                    title="Для этого сгодилась бы крыша одного из соседних зданий. "),
                    components=[
                        Button(style=ButtonStyle.blue, label="Далее"),

                    ]),
            responce = await bot.wait_for("button_click")
            if responce.component.label == "Продолжить":
                await responce.respond(embed=discord.Embed(
                    title="Тех.сотрудник –«Ну скорее для пользы всей станции,чем меня. Впрочем, я её получил сегодня утром и сразу отправился сюда, ведь из за одной маленькой неприятности отключён целый жилой сектор.»"),
                    components=[
                        Button(style=ButtonStyle.blue, label="Продолжить"),

                    ]),
            if responce.component.label == "Далее":
                await responce.respond(embed=discord.Embed(
                    title="Сразу откидываем бар и ресторан здания одно и двух этажное соответственно. "),
                    components=[
                        Button(style=ButtonStyle.blue, label="Далее"),

                    ]),
            responce = await bot.wait_for("button_click")
            if responce.component.label == "Продолжить":
                await responce.respond(embed=discord.Embed(
                    title="ГГ-«Так а что за неприятность-то? Неужели что-то серьезное? Целый сектор просто так не выключают.»"),
                    components=[
                        Button(style=ButtonStyle.blue, label="Продолжить"),

                    ]),
            if responce.component.label == "Далее":
                await responce.respond(embed=discord.Embed(
                    title="Из всем вариантов оставался только мое временное место проживания. В теории выход на крышу на карту не закрывают. Ха, интересная недоработка, крыши не закрывают ведь AI не знает про суицид. "),
                    components=[
                        Button(style=ButtonStyle.blue, label="Далее"),

                    ]),

            responce = await bot.wait_for("button_click")
            if responce.component.label == "Продолжить":
                await responce.respond(embed=discord.Embed(
                    title="Тех.сотрудник-«Случилась маленькая неприятность. Подробности рассказать не могу. Но она аж на северо-западе отсюда так что вам и этому сектору ничего не грозит.»"),
                    components=[
                        Button(style=ButtonStyle.blue, label="Продолжить"),

                    ]),
            if responce.component.label == "Далее":
                await responce.respond(embed=discord.Embed(
                    title="Я действительно был прав и лестница на крышу была открыта. Вид откуда действительно был на весь сектор.Вся восточная часть была покрыта небоскрёбами, а вот в северо-восточной части было что странное."),
                    components=[
                        Button(style=ButtonStyle.blue, label="Далее"),

                    ]),
            responce = await bot.wait_for("button_click")
            if responce.component.label == "Продолжить":
                await responce.respond(embed=discord.Embed(
                    title="ГГ-«И на таком успокоении,спасибо. Мне пора бежать, удачно вам поработать и будьте осторожны.»"),
                    components=[
                        Button(style=ButtonStyle.blue, label="Продолжить"),

                    ]),
            if responce.component.label == "Далее":
                await responce.respond(embed=discord.Embed(
                    title="Как будто бы там специально что то осветили,прожектором или оставили включённые фонари для помощи в проведении работ. Остальной сектор обесточен."),
                    components=[
                        Button(style=ButtonStyle.blue, label="Далее"),

                    ]),
            responce = await bot.wait_for("button_click")
            if responce.component.label == "Продолжить":
                await responce.respond(embed=discord.Embed(
                    title="Угу, значит на северо-западе ,теперь осталось узнать ,что именно там есть и в этом мне поможет терминал помощи. "),
                    components=[
                        Button(style=ButtonStyle.blue, label="Продолжить"),

                    ]),
            if responce.component.label == "Далее":
                await responce.respond(embed=discord.Embed(
                    title="Угу, значит на северо-западе ,теперь осталось узнать что именно там есть и в этом мне поможет терминал помощи."),
                    components=[
                        Button(style=ButtonStyle.blue, label="Продолжить"),

                    ]),
            responce = await bot.wait_for("button_click")
            if responce.component.label == "Продолжить":
                await responce.respond(
                    embed=discord.Embed(
                        title="Подойдя к терминалу и открыв карту сектора H-32, которая к удивлению была не заблокирована и общедоступна. Еще одна недоработка AI. "),
                    components=[
                        Button(style=ButtonStyle.blue, label="Продолжить"),

                    ]),
            responce = await bot.wait_for("button_click")
            if responce.component.label == "Продолжить":
                await responce.respond(
                    embed=discord.Embed(
                        title="Впрочем на северо-западе, единственным за что я мог зацепится стал корпоративный кампус. Там могут проходить исследования, но что бы причинить завал кто-то должен был сильно ошибиться."),
                    components=[
                        Button(style=ButtonStyle.blue, label="Продолжить"),

                    ]),
            responce = await bot.wait_for("button_click")
            if responce.component.label == "Продолжить":
                await responce.respond(
                    embed=discord.Embed(
                        title="Я отправился проверить кампус, если там пусто ,то я ничего не теряю, а так получу больше информации зачем Alife скрывает аварию. Инженера на границе уже не было и я спокойной зашел в сектор H-32"),
                    components=[
                        Button(style=ButtonStyle.blue, label="Продолжить"),

                    ]),
            responce = await bot.wait_for("button_click")
            if responce.component.label == "Продолжить":
                await responce.respond(
                    embed=discord.Embed(
                        title="Путь до кампуса занял минут 25 по абсолютно пустым улицам. Практически апокалипсис, разве что здания все целы. Я двигался под стенами быстрым шагом что бы если что завернуть в переулок и спрятаться от погони."),
                    components=[
                        Button(style=ButtonStyle.blue, label="Продолжить"),

                    ]),
            responce = await bot.wait_for("button_click")
            if responce.component.label == "Продолжить":
                await responce.respond(
                    embed=discord.Embed(
                        title="Кампус. Двух этажное здание с стекленными стенами в некоторых местах,что крайне абсурдно и странно. Стекло крайне плохой материал для прочности конструкции, особенно в космосе."),
                    components=[
                        Button(style=ButtonStyle.blue, label="Продолжить"),

                    ]),
            responce = await bot.wait_for("button_click")
            if responce.component.label == "Продолжить":
                await responce.respond(
                    embed=discord.Embed(
                        title="Жертвуют стеклами в некоторых квартирах, а тут целые стены. Интересно как AI решил что это необходимо.Неужели мораль сотрудников настолько увеличилась что малая прочность конструкции того стоила?"),
                    components=[
                        Button(style=ButtonStyle.blue, label="Продолжить"),

                    ]),
            responce = await bot.wait_for("button_click")
            if responce.component.label == "Продолжить":
                await responce.respond(
                    embed=discord.Embed(
                        title="В округе никого не было и я решил зайти внутрь. Внутри главного здания все двери были закрыты,кроме главной лестницы вниз и верх. Я решил сначала вниз"),
                    components=[
                        Button(style=ButtonStyle.blue, label="Продолжить"),

                    ]),
            responce = await bot.wait_for("button_click")
            if responce.component.label == "Продолжить":
                await responce.respond(
                    embed=discord.Embed(
                        title="Спустившись, мне открылся полный хаос. Все двери выбиты, мебель разломана и везде лежат куча бумаг,стекла,ДСП. Из левого центрально кабинета шел приглушённый свет, он переливался кучей цветов."),
                    components=[
                        Button(style=ButtonStyle.blue, label="Продолжить"),

                    ]),
            responce = await bot.wait_for("button_click")
            if responce.component.label == "Продолжить":
                await responce.respond(
                    embed=discord.Embed(
                        title="Зайдя в кабинет, я увидел кристалл неизвестного материала,которой отражал внутри себя кучу цветов одновременно и отображая их на весь кабинет."),
                    components=[
                        Button(style=ButtonStyle.blue, label="Продолжить"),

                    ]),
            responce = await bot.wait_for("button_click")
            if responce.component.label == "Продолжить":
                await responce.respond(
                    embed=discord.Embed(
                        title="Неожиданно в моей голове начали появляться мысли «Твой путь завершен, иди ко мне», «Я знаю что ты хочешь, иди ко мнее», «Иди ко мнее»."),
                    components=[
                        Button(style=ButtonStyle.blue, label="Продолжить"),

                    ]),

            responce = await bot.wait_for("button_click")
            if responce.component.label == "Продолжить":
                await responce.respond(
                    embed=discord.Embed(
                        title="Этот кристалл действует на мозги? Достаточно интересный эксперимент от AI, он и так контролирует всех, а теперь решил найти этому объяснение для этого мира."),
                    components=[
                        Button(style=ButtonStyle.green, label="Тронуть кристалл"),
                        Button(style=ButtonStyle.red, label="Не трогать кристалл"),

                    ]),
            responce = await bot.wait_for("button_click")
            if responce.component.label == "Тронуть кристалл":
                await responce.respond(embed=discord.Embed(
                    title="Я решил прикоснутся к кристаллу, возможно так я получу свои ответы."),
                    components=[
                        Button(style=ButtonStyle.blue, label="Далее"),

                    ]),
            if responce.component.label == "Не трогать кристалл":
                await responce.respond(embed=discord.Embed(
                    title="Крайне глупо торкатися, то что устроило этот хаос. Вокруг меня было куча документов,понять которые абсолютно не является возможным. Все было абсолютно хаотично разбросанно."),
                    components=[
                        Button(style=ButtonStyle.blue, label="Продолжить"),

                    ]),
            responce = await bot.wait_for("button_click")
            if responce.component.label == "Далее":
                await responce.respond(embed=discord.Embed(
                    title="Положив руку на кристалл я почувствовал тепло в руке и одновременно холод внутри себя. Кристалл перекрасился в чёрный и я почувствовал его «мысли?»."),
                    components=[
                        Button(style=ButtonStyle.blue, label="Далее"),

                    ]),
            if responce.component.label == "Продолжить":
                await responce.respond(embed=discord.Embed(
                    title="Из обрывка документа стало известно,что кристалл хранился за огромной кучей преград. Две экранирующие сетки, металлический саркофаг и тройной слой стекла сверху."),
                    components=[
                        Button(style=ButtonStyle.blue, label="Продолжить"),

                    ]),
            responce = await bot.wait_for("button_click")
            if responce.component.label == "Далее":
                await responce.respond(embed=discord.Embed(
                    title="Неизвестно-«Чего ты хочешь?»."),
                    components=[
                        Button(style=ButtonStyle.blue, label="Далее"),

                    ]),
            if responce.component.label == "Продолжить":
                await responce.respond(embed=discord.Embed(
                    title="Что могло случится? Какой силой обладает этот кристалл? Мои размышления постоянно прерывал кристалл заставляя тронуть его или начать с ним общение. "),
                    components=[
                        Button(style=ButtonStyle.blue, label="Продолжить"),

                    ]),
            responce = await bot.wait_for("button_click")
            if responce.component.label == "Далее":
                await responce.respond(embed=discord.Embed(
                    title="ГГ-«Для чего ты создан? Что ты делаешь?»"),
                    components=[
                        Button(style=ButtonStyle.blue, label="Далее"),

                    ]),
            if responce.component.label == "Продолжить":
                await responce.respond(embed=discord.Embed(
                    title="Первое решение как прекратить вмешательство кристалла в меня- разбить его. Взявши ближайший кусок ДСП я замахнулся и ударил…."),
                    components=[
                        Button(style=ButtonStyle.blue, label="Продолжить"),

                    ]),
            responce = await bot.wait_for("button_click")
            if responce.component.label == "Далее":
                await responce.respond(embed=discord.Embed(
                    title="Неизвестно-«Исполняю желания. Смелые, глупые, страшные- любые.»"),
                    components=[
                        Button(style=ButtonStyle.blue, label="Далее"),

                    ]),
            if responce.component.label == "Продолжить":
                await responce.respond(embed=discord.Embed(
                    title="При ударе по кристаллу образовалась сфера энергии, удар по которой устроил выброс энергии из этой сферы который снёс все стекла в здании и отбросил меня, знатно приложив по стене."),
                    components=[
                        Button(style=ButtonStyle.blue, label="Продолжить"),

                    ]),
            responce = await bot.wait_for("button_click")
            if responce.component.label == "Далее":
                await responce.respond(embed=discord.Embed(
                    title="ГГ-«То что ,здесь произошло, желание?»"),
                    components=[
                        Button(style=ButtonStyle.blue, label="Далее"),

                    ]),
            if responce.component.label == "Продолжить":
                await responce.respond(embed=discord.Embed(
                    title="Спустя время"),
                    components=[
                        Button(style=ButtonStyle.blue, label="Продолжить"),

                    ]),
            responce = await bot.wait_for("button_click")
            if responce.component.label == "Далее":
                await responce.respond(embed=discord.Embed(
                    title="Неизвестно-«Возможно»"),
                    components=[
                        Button(style=ButtonStyle.blue, label="Далее"),

                    ]),
            if responce.component.label == "Продолжить":
                await responce.respond(embed=discord.Embed(
                    title="Спустя неизвестное мне время я почувствовал боль во всем теле и особенно в затылке. Сколько я здесь времени и почему меня никто не обнаружил? Я устроил всплеск энергии на целый сектор."),
                    components=[
                        Button(style=ButtonStyle.blue, label="Продолжить"),

                    ]),
            responce = await bot.wait_for("button_click")
            if responce.component.label == "Далее":
                await responce.respond(embed=discord.Embed(
                    title="ГГ-«Я хочу,что-бы кампус вернулся в состояние до твоего появления, а ты и этот хаос исчез."),
                    components=[
                        Button(style=ButtonStyle.blue, label="Далее"),

                    ]),
            if responce.component.label == "Продолжить":
                await responce.respond(embed=discord.Embed(
                    title="Задаваясь несвоевременными вопросами мне удалось сесть и предположить что я более менее целый и могу передвигаться."),
                    components=[
                        Button(style=ButtonStyle.blue, label="Продолжить"),

                    ]),
            responce = await bot.wait_for("button_click")
            if responce.component.label == "Далее":
                await responce.respond(embed=discord.Embed(
                    title="Кристалл исполнил желания как ему велели и комната с кристаллом и главным героем оказалась посреди пустынного космоса, а Яр так и не узнал что случилось на станции «Омега»."),
                    components=[
                        Button(style=ButtonStyle.blue, label="Вы погибли"),

                    ]),
            if responce.component.label == "Продолжить":
                await responce.respond(embed=discord.Embed(
                    title="Я решил что не могу здесь оставаться. Ели встав на ноги я посмотрел на кристалл. Он абсолютно не изменился.ГГ-«Бред, что это за туфта. Зачем этот кристалл вообще создан?»"),
                    components=[
                        Button(style=ButtonStyle.blue, label="Продолжить"),

                    ]),
            responce = await bot.wait_for("button_click")
            if responce.component.label == "Продолжить":
                await responce.respond(embed=discord.Embed(
                    title="Я ковылял в сторону своего сектора H-31. Тело по немного возвращалось ко мне и немного отойдя от кампуса я смог полноценно идти на двух ногах. На удивление в округе так никого и не появилось."),
                    components=[
                        Button(style=ButtonStyle.blue, label="Продолжить"),

                    ]),
            responce = await bot.wait_for("button_click")
            if responce.component.label == "Продолжить":
                await responce.respond(embed=discord.Embed(
                    title="Возможно Alife не умеет реагировать на такое, ведь никто не учил его на факт вмешательства, теперь ему нужно время что бы проанализировать мои действия и адаптироваться к ним."),
                    components=[
                        Button(style=ButtonStyle.blue, label="Продолжить"),

                    ]),
            responce = await bot.wait_for("button_click")
            if responce.component.label == "Продолжить":
                await responce.respond(embed=discord.Embed(
                    title="Дойдя до своего сектора я понял по имитации солнца,что уже поздний вечер, а Яр меня не вывел. Максимально странно. Он не мог ошибиться, он знает что его ошибка дорого стоит. "),
                    components=[
                        Button(style=ButtonStyle.blue, label="Продолжить"),

                    ]),
            responce = await bot.wait_for("button_click")
            if responce.component.label == "Продолжить":
                await responce.respond(embed=discord.Embed(
                    title="У меня есть еще один способ выйти. Я дошел до терминала помощи и вызвал аэрокар. Сел в него, выбрал ангар дока D. С кораблем точно ничего не должно было случится, его должны загрузить и оставить. "),
                    components=[
                        Button(style=ButtonStyle.blue, label="Продолжить"),

                    ]),
            responce = await bot.wait_for("button_click")
            if responce.component.label == "Продолжить":
                await responce.respond(embed=discord.Embed(
                    title="Прилетев в ангар,я зашёл в лифт и выбрал этаж 2 «Док D-2». Выйдя из лифта,я застыл на месте."),
                    components=[
                        Button(style=ButtonStyle.blue, label="Продолжить"),

                    ]),
            responce = await bot.wait_for("button_click")
            if responce.component.label == "Продолжить":
                await responce.respond(embed=discord.Embed(
                    title="Корабля не было, захваты пустые. Я подбежал к краю и увидел что случилось. Моя авантюра создала заряд ЭМИ на станции, захваты отпустили корабль и он упал вниз на жилые сектора станции…"),
                    components=[
                        Button(style=ButtonStyle.blue, label="Продолжить"),

                    ]),
            responce = await bot.wait_for("button_click")
            if responce.component.label == "Продолжить":
                await responce.respond(embed=discord.Embed(
                    title="Я стоял в доке,смотрел в низ и видел огромных размеров пожар, хуже только причина этого пожара- мой шанс на спасение."),
                    components=[
                        Button(style=ButtonStyle.blue, label="Продолжить"),

                    ]),
            responce = await bot.wait_for("button_click")
            if responce.component.label == "Продолжить":
                await responce.respond(embed=discord.Embed(
                    title="Теперь я без временной карты, преступник за проникновение в сектор H-32 и аварию,в следствие которой убиты и лишены дома куча людей. Я не знаю когда вернутся в мой мир и как жить в этом."),
                    components=[
                        Button(style=ButtonStyle.blue, label="Продолжить"),

                    ]),
            responce = await bot.wait_for("button_click")
            if responce.component.label == "Продолжить":
                await responce.respond(embed=discord.Embed(
                    title="Похоже теперь это «Моя Реальность»…. "),
                    components=[
                        Button(style=ButtonStyle.blue, label="Продолжить"),

                    ]),


@bot.event
async def on_message(message):
    await bot.process_commands(message)
    msg = message.content.lower()
    if msg in variatiprivetov:
     await message.channel.send(f'Хаааай {message.author.name}. Как настроение?')
    if msg in variantinastoeniagood:
        await message.channel.send(f'Не тильт ?0_0?')
    if msg in variantinastoeninorm:
        await message.channel.send(f'Почти тильт, пора умирать')
    if msg in variantinastoeniebad:
        await message.channel.send(f'ТИИЛЬЬТТ')
        await bot.process_commands(message)





@bot.command()
async def pomoch(message):
    await message.channel.send(f"Как дела бот?-настроение бота")

@bot.command()
async def SendPapich(ctx):
    emb = discord.Embed(title = "Papizi", colour=discord.Colour.blue())
    emb.set_image(url = random.choice(papizi))
    await ctx.send(embed = emb)

@bot.command()
async def Papizigif(ctx):
    emb = discord.Embed(title="Papizi", colour=discord.Colour.blue())
    emb.set_image(url=random.choice(papichgif))
    await ctx.send(embed=emb)


bot.run(config['token'])
