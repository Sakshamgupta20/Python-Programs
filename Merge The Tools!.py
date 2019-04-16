# -*- coding: utf-8 -*-
"""
Created on Mon Apr 15 17:38:47 2019

@author: Saksham
"""

"""
The first line contains a single string denoting . 
The second line contains an integer, , denoting the length of each subsegment.
"""


def merge_the_tools(string, k):
    for i in range(0,len(string),k):
        fin=[]
        x=string[i:i+k]
        for j in x:
            if j not in fin:
                fin.append(j)
        print(''.join(fin))
        
        
merge_the_tools("RDITWGZKCERWXKIINHSEHTAUJYNNUEONHZGGFIQHMJDMTNUJUOPDIPARONGKTVYDUGJBQBKFLNRGCNRZCHEKWEBMUIZNFXQBFBCWFMDSBUYFJSGLZLXXPZKLJJZQIRRPVVNAJQSMMSTWKAHJNHHEGTQREPHOIADDVRFGHXSUSLSCNBOAIXFOSVHWMOKWOPALGHRQFLMZXEBKFRNOQSEINOEBCQXTIZGOHYGOLSNKWQVEIKUYCAJROPSTIPMQPSEYSNMEFZOEPLIZVEAXELQVAIOIAAYRUFPNSBTZCHDTVNTQRVQYGGTIRHRRJRIDWZSQALQCVVXSJQKCNACVJVECEXVPOFVNEPFEBXIYTFQEYAGNDJLOGRSNONCESZTWPBCSYMQTRIXRKGHPRSFXJXMZMPDEOZAFAEXAQPUKXTDKZKBSEHSNGEMTVSXKTARVGPVXERJELMOMZPFDYXTFBHAZBZLUZCPIRNHWEQAREQEFHLJGKENNLNMNMXHOAZWRMDPQVRKZHOFRBQXLUMAFZNUNKEBMDXGPCVHXNTZWJGPKWMXSYYZZLUNXYOKDOQUSNBQCVPBEXQRTFONDOMFBISZGILJYDFRQHJVEAWKXMDSRUFXIREKAWJIGWUHZZYRIHMOJKBGXEYQADPJWTTYREJYCFFBGFUROJFXTIFSPDLPIAAGUTHNZSLBXSEFZZWPKEMDMTYDWJVGJVPFRYTQQGSPBYUCXRSHXGNLALPYWKFHHWNYUIPKQJZTHVWHMQQLWFXWQMVOYCWHALGUTVGLGHHNCFWRVNERSBQLPNZPRVXRGDNBAVPGEWVIBSBYFGRZHJKXWMMPJLIQOXTOSKWWISFLKIJRODQWMDVLPHAYTLQJIMABYWZHOGSAPERDHKBVNWGEGJEBUXKCLKFJHHSXNLYERRIABLVQIEWONBPJABNLMTWVAPUPCSUTMEVNPSGXYCLLFCWHEKSSDRPFGJUIEODQSAFISNHRSTEXXBHDNZVSSMXYWRICILUALBKGPSXHNDGKENOTPLLHYIGWCOYKCUMNVXVKPSRCWAOCNEWEQJMQUUOWKOIMIUCDRXOGSHKOHZSXDQBVANNUJBSUPAGXUKDOIRWAAHQKGIHLZKJBAWXJARDPTMPNWSDGLAGLHWXPHECIRLJRIICIZIZSUOHQILXVNFJUEGLLNNTEZEXJOZRNHSHDJQURDTNQAYMEEXRRLMXMQUVEWOTDGCHPTDJWYYPAWBFAZYUMLRADOVIKJDPRGYHZDQXBOMEKOJMPJGDUADYOAIALLPCTQJUTBSXPGBBWMQLVWQQYTQOVYOGLGJFWSZRWTONARPWDHKBDCTEYJSTHJASPJZNDBGZUXPWOEVULHVQJOWHXPBGYBAPMAERBKRXHIUWMPQZWNRFBOPYFQGFTGUHIYYJKRHSZDQNSIOQVIXWYMWDECIZIEGTCFCMYLGAQWNKECAZMYXKMTNRVXQGBXZFEDTERAEHYSSFWUGKUEUHXJAVGQDJPEQVHJAALGIMACRYYXITBCCBLCWTUZEKDUHMGJNRQXDQBWPZUXUVCWWPYUJVVNFAKONQYCJOBPGCLXDFVYDZUBOVYXQTNXWZNJPLNABOPISBFVICTNBQRQLPPDKECGDPRSBEVEUKMMNUIYYBNARESEVJJIOLORBIMEMHKJTXVHTFHRJUTCBNHWXSELEVEHDSNRBXAVWYEPDLJMHCRISYFPQLCWGGFLBSDCSFXODBGJORXWVOENOLCHXEFFNLROFUQXZQOFTUQILNGGEKUUWYDVDJASURGBNYZNONUKJKSUZACFKYAIXDFCOGUKZCMNALARAWDJIXFHXHPJIRUFWZHLHDVHFHUHUWAUSDDAAKJZUAJCRDHOEQZMTWTAENHAJIVDNAFQNQPHRAJIFQWKIXWBURBAGKARUXUIABANRRUISDRXVPJDNHGJYJLETLXOLRYLSYAMPUUJZLJWDUBQCHBCQMJLZGZKAXXUXXGPTBAUOJSRETJICKKUWTGWCFGCFGWEFDTBEUXUFQMJJVTOGEIEZOADWJFBPEFWHBXNVVJCLVOWTHMZNVFPJGSHPAIGEQENTCCQZLSMJGKCQXDDSISDONLFNVNTNSIGWKYVVRJGZTIPQLTKUNQKABSPYFIOZQWXCVUAMDGLZPBPCWCYJSLMVDBVKMJMEGJHBEJPJPAIGDALZCJLWWXRZYOMMYYRGJAJNJYZAAHJGHUHJFSHCPYBQPPCNNVVXVEMGENHGVQOCMWOROXTGYXWNMYCCUXZRDNYJDHRYZGCNCSESQYYOXUBJVDLRCMIHCISFRJDSPHFTAKOSKMGJJJSGOEXQSHZUSRBLAEESOLNOXBGJQOSBXLHLRGDLNCGHTHTVOZNEKDSKEATWQOXNBGASMDDCHLJAVEXLDLPQQJCULXTBLSQMBQGNVMRCZDEUHBHNOYFEJHBUEWXSONEPFLFAZWEYBIVJMCYCDDJMMKJSGGKWWRMDETGDRKBTVYCJBCLGFUSTGDLOKYLIRZLVSTALEDEBCIKFKXLPSFKAJYPVWAFPBSMVMMGQRLTTTDAECNVWTGXEEMZCOGRRYDMKRUCIFVEBAGFFUCBPKYTQMUSCALVAQHLJCPSJLYKNERSAWUPGUKXJGRNIFJJVSWFWLZGYXSODMIEIEVQZIPKOHXZOGKJZGQVTRDSQYIUKQAUVXMWFCIWLFVZOFKPNDMGUQALQIFCBHWYEIUKMCGXJDYXIJOVMBDITETJOALPHJNOTJAGNGFXJEWTPLQDMTLFXHQMHBDRMRFFCFNQNVNYBJTQUJVICIPCPFQXITQUMVCPCPFPKUPLDIDARYKVJAZYHPXQLNKZKOQMEXDQRSEXCHZTIJRRLQRTIPJVCVWNKNBQKFIEZMBCUAXELOXXHOSRDDOIYMXKZYCMFLQFXTHTVEZIVWHELZXQCNYDZXNBWSPBDHGAAPWXWVFTSNZFMYVRLWUMVJPRBEVGLDJNVFKRASKUFLBTJZKWVGISQAKTEHASKJFFQSYSKKPRVQKGPXCMFNFXNRRRYTLKETSULQOXDDQYUCHJZJWHYDELUXFSQQEWJWQWPHVSKLSEOBQPLOWLRBXLYEFRULNGKGEZNATZLNEBPWRCKPNDSMQRQXKNIXVSFZTUZMUNCAOTWHVIXKNRXDINAUCIUXBZXUUYJOLLOCGMJBWILJAKMKYMHAWBAZAXUWVFKJSALYOWZKFMVHXHTXVAZUBZTEYNAUUNDMNQMEMLQTAMAZVWYTWXNAZGEXWERQRWFHMRNBFDUFPXGNTEGRBTRAZXAVEROVQTEEKRFPXAWOZEBSIHLMCDOECOBGIPEYKIEXCKOZMLNLRPFAYQODVCHYTIGBAKBMVFJXPYYDLLQCCXEDOSGLVNLQXSRZESMZXVYPVWUGILJMKNPYIXMFMZVKRMLYGXZFVYWQURZEEITOXIPFGBKSCFEWTSUZRTHMRDFOUEUAONRLYGTGJFALNHHGZDIQXPFQSMGPQBRGQITQOMWZUZLHIUPHYXZXOGNJSWAKXRQPAKGQYEQSFDBNXRWXQWUFEKQXGQJDHAUHMCYKJQFOTGCSZYQQWKVDULAABJFKLCUXESKNKPEDXGVXGLNFYKIUXKXAVCKHGEGLYSAIJENHMLGVYVAWFITEUQEPUQYBXHMXZOIJTVSHIYCHTCFAMYEGOKYJCWKBFYZFOHOHEIRNGTWBWBDKAHTOTTZXRJZXJACYHSHNAYCGSYJQAMCAVVQQOQNIBOFLOHLXZSLBRNJLMSDMEFOBDERTWGBYVGJJPUHOOURHHASVSVJYDZZGESZAZDAUJLFZHMPWIHDSHYNCVZCYYCGEUIHTLHPWTVVAJNWSWCMFAZHVAKWZOCDKKKGXUVUNSRPCGOWCQKIQJPNMBJLROQCADIAXFUMYNBCURAYHKGZVYPHBAUTONVRQDRPINDIAGKWYMVFWBHUBWBDWYWNLREDWVSGIVPKDBJBOEJMHQGJMKOKIKXVDDYBASHKPYVSCEUQKDERTLCHXSTFERAHWAKXSSHHSEZUKVMUYROTESCBLWIPPKZLKJIEDSNYWMSJKHDIATEEMGHZEROTBPFNBPTGJGEIUZREGWPGQTMCBTBGKRBNJGCKYVQJBVRXUICCHTKXMWBPRCXDVZQEHUQHPHRSEKRATTCCMMZAKASBEPEBQWGAQWHHFYBJJSJEONGABHDLHVMNMSOFOWFGTMPANQKYJVCXJKZKTEWAZKPODDTTAYCVKRVZIFXTBBSMLRWEYSGXFVNIBGDBEFYRXTQHBOAEPSQDLOJJJSJOPWYQFBTJJRCINVPQLPUCJMFWARGJLRXANXTSBOEKIISVDHLQYHTHVADVRLHECGHSEAMFQSPYBJVGSIXQRQZMQCIKQPOUXVMBXZGQRXOUGMBYUAQMSPAKUIUKZLEXITAIUHYNGMINALNVNEJFVJPPUMBVZIUHBXPXEPKMCUBEHPBUVKBSWRISFLPETMNWJDTPSGBWADDIUEERPGJNZTHEHWKAKXZTCUKXAMTDRYNNDRGUZRHYNQCUOOWZMVSOQFLSRHXKFKXIEDCDWLCJBGDQVAPJVJXNOJIHSFRXSQIWVKBSYFBZMHRJHISEURUICESULLUDECBZOFTMKXOYEFHLQBRKVLUXPMUBYOGCSKDIPXVZWLYASHNILESGSNFJZZMZPTDJFHSUGPTCARESBRBMXVSRIZBKZPLQIPANYSJGHDIJWOBXFELEAFWKFZUGOGYZXYOVSYBBBLKZZOZGSMMUSIFZJBFYHDXEELBYLEAORMOSCPAXBNRTXWUHABHHHEOLRRLDWNTPAHIEYIBAXTVVRQERRLBYRRLKIXNGKHWMQGRPOURMPMJHENAWYDWRUKBFHRLTAJGQPZHGTYSJNDSRQUPQAOJUYKBHBNABYIUOHDWDEOORTIKJCCBESKZSWAZYPBBQKVGTBCYFSMYLUKWZOZDGJEYFHZFYBHQNEWGFAFMSTKDQVBRLAWSLBSTKUYKVHBKMZQTAXGSTSYJPBABCYVNZNGLJHYGOBQCAJYAGEVZYVKOWMPYLKOMZWYJDYPUZIWZRUCXAXZZSLPOYEPJQFVRBVCHTSBSAZSRWUQYTRZLDOBBUSKMXHEZDGIWAJPCKJVIDOHYFGJKXMNRFZGCHKDKSLGVWXXJGTRLHAJOJUBGHOZOOFSXRYHMLPHIPETVZKJINSXWNYEWODMELEBECKQQAXYPCRMBDVMQOJODJSBZWNEJTHNYSEOUBOLFHXJKVVDLGRORKRQIEURZCEXWKLQOZBTGAETVZWGFPWWBNPJTLCTNJQLTEBHDCDMDHHAHDHOUDNWTCHONKHDTAOOESWJUZXZGEAPJJGEOTCHXJWKTFPOFGDLYZXSAUUIBWAKFGQTZSDWCZIVGYKOEPZEQYYQTSAWOAGVIXRHPUFTVQPBQBPWQRAGPYYKRYGHBPFJOWTDQAZLQQOGRGEJXEPMDPZWPFFQUKCIIXOAXNLODCWWIBFFFWTKLSICAOVUAXFJUVLRKXHPBGLJHSQOOLBBEJFEZAAAXHLTCWNMVUDWCOHJGZAWLBZRKFVKFXMFFZYJVNYTKBRMSZYAAYXLBYCNFZXLZLSGKSPIGPBSTSELTCLUCKHDJMROLQBKCVSOOKWWZZOSSSFNXRJZBRDMFWDQMEDQCXFQHDOHDCBXWHKVAWVDPAQUWTMIZRZBPGTWJJFMNJLMSWHSUEVJENFCIRNIJMLAUHYDSGSGPDSHBBBXGWGMKLPUFCEQQQQKZQPRWJZLNTUQVVOBUWNGKEAPIFFYXXKWNCPMLRZAKURFPHIJDYPNCQELXLLUIWSYYJMLALMLFFQXMZGRXYHBQLONXAHHYBHYKTJLFVWKCOHOPQGOQPQGAGVZGCJGFQEPKOARLYBONLEEDMTTBLZERUDYYMGDDLSPBVGOTJEIUJNXVIQZTRDMLIMLVTOAEJRFEXVZIAKFJXEGHVFAOKOCTBNQUESANJFTICUQCEVNBAUKXBMNOBPHCFZYJRYYAFRKHLAKSYXTATGZVSOJTESXJRVUITSKYLUGYWQQWPMWJSXEMMPGSHDDYZXISRSTEMZEKRVHGJFPDDTPRKXLRBORCNZWERPKFQOQHLXOWCDZHXPAJMLBPZSTOUQUNHETYVLFGKTDMXCWWTYFIKGZLBTAVJUKSBDQWOWCYPHNOMLKHJQPTYRHBKHYVBJNCOGADCDDTMSIYDSGPKXKLORMAYNXCWNGKTJPVMVOYPYZVRFKDEUOVODVOQVSOIBABKSYYPOYEPXZGELJJIAGWDBMVYFLGGLJSFJQUAOZPMAXSMIDUIJQNNCKLJVUPJDHOPZJPOKGCKDUWLYQWJIJWNUIWRCOAHXPWXANLKVPUYJTMJLKVUVRJRBFJFTJNTYLQABDKWSHXDALPLVKHSDQKFYTMREZMFNCFQHQOZZNFZAWMVGWQLMASKTFEXEQCTVKJCAAEZNJAOFOLNKBYXBRJWWPWCIAYDKJHMJLNZWPPDEAQOERNHKZEIOCMYCKDPWLDFYRGVGVYKWRBCIOJUNNCEROCUBGLXTOERHLMOGNAEEBGOSQKFFMLZCQTDWGCPWHIESXUAKUHQYPGQHQXNCJMGZHKXPMOLVWRPTLQFGZVEODUWTTLXCZEDIOCZCQKYPCNKNFQVENBVRXRKREIVDOZNCDMGWYGLAUVQBNNGBPBSMUEDYOZDCAQGDENZCTMFPKXRXKZAZCUOYBRWPSBSUTAAXNBBJOGAADTZQSAPWWDUXXSNRTHMOHMLXNPIDVKDBEDRYFIXBORZNMOEHXSWGEJFUYPXWADXEGQELABOOVPDHDIOAAKJHWOBUEASEDPKJHQWISLWNCAUGKKIMXRTTIUPMVISYZEKHUIPOVNBYPXEBKOOHIHCQEREBBYBBENKAWZPROSPGSVHCMVJUFNMLGSMISNLWBVWZWLQMGISYFCATXLNEYBPETBOLRZJUWGTSTLFZTZZBBZUBMKHKLXRHAHUTHENDKIYFUFHPGGQIINLUXSHKPYTSFOLOSZUEJUJDZSTFZLPHAADZVKKKKDEQTQGLRARAUDEVVZDWMUDNXJMSTYCECJWVZCJQFASBDYZBZEXMYBZVKNNFMSJQBHNAKYSRZMUELTFKXDWYGXTSNHZBZJRCSGCCFWVGIQMVLUGLZEJFECZTLYUMJNOCVSGCOEIZWXUJRCUSJFZNKYGVYCIKPYOKRWNHAXGYWDIPFEHOKGDUGLRHNBREAHRRDGYGDHECKORPTBGDHJZOXQXMUORUVKLAQLGVSNXCBRUUSAZZLAPKRMXLCQHZASAQFILYVLCXCYTUATVMTNYMBVZGLGFLAHBISPGNAKMCJIYJBVXWKWLMTKUFTZSVJWDBLLQLYFPHNPSOKSMXOXLHKFOFGHAPDGSQTJBROSABJVRVNFSDFDMPIBWPKWGPEZFYIIRYAUZJPSECZZFECRTNUPCEOITUJYURGMPIIQTXKAZKZGOBXKQSBSWRDSMMQIGZWXHEODBADAMCGBFGNWAOQWIVQUKJEQIBPRFDUHGXJSZSVHYIDYZVWHRNDBWHTGIIXOOSXURGORYKYYSDWTYVCPKHSIRNOZWLPKFOGXVUQVEQUZTSUTNXLZEDHXRVXPJOBQFHNADDXKVRLOMHKBEVBLYKIRGHIRYJHDSXFYCCIYWVMKCYLJTOUUZENHOWYOFHRAEYYHAGHYDTIFUWONKKHJRVSFRQTYAMYGKWNMEULHQVPMRDZEQHNHEGOVYJTAVUHFQWTXTGELCTXVZWZPFPYJXMEXVAYSWFZODSLWZSHDNEYMDADIRDSORYLOALGWSFLWAYSZQCEEIESLEYWVBQLTOZHRMQPFVABVZVWRZAVIHQVLORJPHWKYXUPKKEPFHSDIPBZPEXXLNSYBMJSVGFTDZKNJREQYYTIOVJDZICMVWKYIUTEAYZFXKVGDBWBASLOPURQDVCAROBAIUGKUHSRTNZWOXZQPKEGHXYMSAMKPPMZJUKDBCWVRVRHTRYKDETKERWWULILAWKMQWRUAORTJKBEDBRHHKTLBQIXDSIDPVPHRJDUXUNIFQNIRGRZQLMTDWRGPBLGWDNQMTKJNZTUQGDJMWKEJZAMVTUKUIQTNGJZZVKOWDJOMOAAKMHWLHKHAFRWPKPCSADTXPJUSSKGIKJTXQRIZBPBIJXXVPBNPEINTRJOMTWUEFPDXGLWIDXQMXQJMRYBYGQTZBHLVEGBLVEJERHOUHGIEWTQQRTQXMJXNRKKXSLIORTUJBIFIOQOLJGDBZTANCZBVKLUCZDSQYMZBUHLLXZYIHBJHWKWALXWVLQYKVQAWFCXBJJMIKKSSNCBJOXKZXIXIYVUWNUSUYPWJAIRNVKFIOIUEHEFEMCOMZIIPFCJDSHNUSGHNSOXIYRMGXUMLYBYALIPQLAUFKJZCPJRIZOSYIFGFBSTZVRZHBQZMRVTBETDWEWGDKYDUFJCGEVGZOHGPYIEPDXSISXEWTMCFKHAQREWVZEWNMFCKNGBQGTAYQGXLSZQDGSVZWRWVYTKKYPUNXVDDOECGKZRFAJIICDIAWGYUZIGZXAMVXSANYCVIDMPDWXMACWABCYXCJEDGGSDGKEVIIRSMDIPBHDDMZENCCMGLSJUZBZHNDCXOTQAZARCHVGVUKKYOXECPQYQTXXHDAERVWTUWKXGFDBCPMADLHFAXFTQDSZISEZQASKZCJFKMIOBWQHHXOKWUDPXXOHSUGIXASWEEDQQNEUKVBRSRBRLGGKEURWRZGOZAMEERWXEBROWUIQLLHZSNJYKDWDCCTECFKHYGEEHXTDTDWGODFITRIDUEGYIBCNIOWGVCKCZFIUIEAZJGHCZQHVWPTHQYUYMQEHSRMTYWNJANILVPOUHVRELLLBLHCZXGJRZVKYTZHVOPGKGUGOSAUFNHGYOKXNTIESFQSYRBTFSARZWAPOALTNUCNIMMXFVDAAVSZMWUTOUNPRNEHPRBCLFPVRDUZYXZBSTAGPWAGRNVKCCRRTUVHZMERPZSOWTPRMRXENZKGOHQSJIJFCGMESQXIPPWOINFWGECTGOAUWSPFCYKFFYJZPIHGXFUHSBDAGIUOWWKUOZATAMYHLJGCTOKQVFXOICOQMKEJIPDZQFSQSSXFDEJWUTMPALFJPWBCGGNRXSQNYKESCDZFJIDDDRTGCAPTWSVFAKWXDONDYTVCYWHIGMLJDGPFHGYFBWKBGIBLWQOWJLYHJHRPTDBWLSDSBCACAKFITGWRWKOHYORHWIXPNAMZUPTVTTZVEFEZNASKMGTKXKUTVTIITWJNMDLHWKDCPJDFLWPZEKMBXGUSZFCUBMHPRSXPFCSWNXBYTSZYDLBARYUSDYMGMUYDOXTTZNSOKTOGMNGRZHTSHNLKNXTARTFIQADRNVFAPTGBGMSHVLADALPPIIPCBXKTXNKLLRNAKTDTHXCCKCFMPVBYFTCJQMCNBPAMGNOTIROPQQUATBMKWQIEJKPZYTOCIPOPEFKPWYGPOAPJCEUAUEGDRVEPPSTXJIOOPADLYJCPMSAQWWQSDXVUUZLJTFJDPZRECWRAHURVMULKQCCTBZNXABHTGSWVTPBVNSYVOPQCJEMCIQVJRLGTMPNUJLRDDSYQMWNBOGDXKSZSKXDEILXWDMQMYJPBBQTPMHSANYAXQBRCYUGIHGEKSWZQFOTGGNYTUQVHOXGGZXLXTTICZMNSJMKOCEXJTXEPNBYEZEKYDXXYRFAQUPKFBXVGBSPWRVLHWJLVPXVUVVUOCUEWKRBNOZVRTKNLHASELDBCCXWXSSLWMSTYLWOZVJQPWFCDHUJSZLWBIUBCMMYYGTZRSNSPYKEUPGAYCJSBUODEIEGUSHVBCWUULNKJXQGPZGNBPGDMWIQFOZBIIYJKUGHFTRRSJXHIFXKWFPIBZBINCKXKIJWDPDKIWBCGAMQFJCCQRKRSNAFPMFBUOAZDFKNCNPKODAVODXEWKYPXAWPMBQG",1246)