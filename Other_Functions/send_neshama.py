﻿

def Func(letter,Bot_Variables):
    neshama =   [
                "אַשְׁרֵי תְמִימֵי־דָרֶךְ הַהֹלְכִים בְּתוֹרַת יְהוָה׃",
                "אַשְׁרֵי נֹצְרֵי עֵדֹתָיו בְּכָל־לֵב יִדְרְשׁוּהוּ׃",
                "אַף לֹא־פָעֲלוּ עַוְלָה בִּדְרָכָיו הָלָכוּ׃",
                "אַתָּה צִוִּיתָה פִקֻּדֶיךָ לִשְׁמֹר מְאֹד׃",
                "אַחֲלַי יִכֹּנוּ דְרָכָי לִשְׁמֹר חֻקֶּיךָ׃",
                "אָז לֹא־אֵבוֹשׁ בְּהַבִּיטִי אֶל־כָּל־מִצְוֺתֶיךָ׃",
                "אוֹדְךָ בְּיֹשֶׁר לֵבָב בְּלָמְדִי מִשְׁפְּטֵי צִדְקֶךָ׃",
                "אֶת־חֻקֶּיךָ אֶשְׁמֹר אַל־תַּעַזְבֵנִי עַד־מְאֹד׃",
                "בַּמֶּה יְזַכֶּה־נַּעַר אֶת־אָרְחוֹ לִשְׁמֹר כִּדְבָרֶךָ׃",
                "בְּכָל־לִבִּי דְרַשְׁתִּיךָ אַל־תַּשְׁגֵּנִי מִמִּצְוֺתֶיךָ׃",
                "בְּלִבִּי צָפַנְתִּי אִמְרָתֶךָ לְמַעַן לֹא אֶחֱטָא־לָךְ׃",
                "בָּרוּךְ אַתָּה יְהוָה לַמְּדֵנִי חֻקֶּיךָ׃",
                "בִּשְׂפָתַי סִפַּרְתִּי כֹּל מִשְׁפְּטֵי־פִיךָ׃",
                "בְּדֶרֶךְ עֵדְוֺתֶיךָ שַׂשְׂתִּי כְּעַל כָּל־הוֹן׃",
                "בְּפִקֻּדֶיךָ אָשִׂיחָה וְאַבִּיטָה אֹרְחֹתֶיךָ׃",
                "בְּחֻקֹּתֶיךָ אֶשְׁתַּעֲשָׁע לֹא אֶשְׁכַּח דְּבָרֶךָ׃",
                "גְּמֹל עַל־עַבְדְּךָ אֶחְיֶה וְאֶשְׁמְרָה דְבָרֶךָ׃",
                "גַּל־עֵינַי וְאַבִּיטָה נִפְלָאוֹת מִתּוֹרָתֶךָ׃",
                "גֵּר אָנֹכִי בָאָרֶץ אַל־תַּסְתֵּר מִמֶּנִּי מִצְוֺתֶיךָ׃",
                "גָּרְסָה נַפְשִׁי לְתַאֲבָה אֶל־מִשְׁפָּטֶיךָ בְכָל־עֵת׃",
                "גָּעַרְתָּ זֵדִים אֲרוּרִים הַשֹּׁגִים מִמִּצְוֺתֶיךָ׃",
                "גַּל מֵעָלַי חֶרְפָּה וָבוּז כִּי עֵדֹתֶיךָ נָצָרְתִּי׃",
                "גַּם יָשְׁבוּ שָׂרִים בִּי נִדְבָּרוּ עַבְדְּךָ יָשִׂיחַ בְּחֻקֶּיךָ׃",
                "גַּם־עֵדֹתֶיךָ שַׁעֲשֻׁעָי אַנְשֵׁי עֲצָתִי׃",
                "דָּבְקָה לֶעָפָר נַפְשִׁי חַיֵּנִי כִּדְבָרֶךָ׃",
                "דְּרָכַי סִפַּרְתִּי וַתַּעֲנֵנִי לַמְּדֵנִי חֻקֶּיךָ׃",
                "דֶּרֶךְ־פִּקּוּדֶיךָ הֲבִינֵנִי וְאָשִׂיחָה בְּנִפְלְאוֹתֶיךָ׃",
                "דָּלְפָה נַפְשִׁי מִתּוּגָה קַיְּמֵנִי כִּדְבָרֶךָ׃",
                "דֶּרֶךְ־שֶׁקֶר הָסֵר מִמֶּנִּי וְתוֹרָתְךָ חָנֵּנִי׃",
                "דֶּרֶךְ־אֱמוּנָה בָחָרְתִּי מִשְׁפָּטֶיךָ שִׁוִּיתִי׃",
                "דָּבַקְתִּי בְעֵדְוֺתֶיךָ יְהוָה אַל־תְּבִישֵׁנִי׃",
                "דֶּרֶךְ־מִצְוֺתֶיךָ אָרוּץ כִּי תַרְחִיב לִבִּי׃",
                "הוֹרֵנִי יְהוָה דֶּרֶךְ חֻקֶּיךָ וְאֶצְּרֶנָּה עֵקֶב׃",
                "הֲבִינֵנִי וְאֶצְּרָה תוֹרָתֶךָ וְאֶשְׁמְרֶנָּה בְכָל־לֵב׃",
                "הַדְרִיכֵנִי בִּנְתִיב מִצְוֺתֶיךָ כִּי־בוֹ חָפָצְתִּי׃",
                "הַט־לִבִּי אֶל־עֵדְוֺתֶיךָ וְאַל אֶל־בָּצַע׃",
                "הַעֲבֵר עֵינַי מֵרְאוֹת שָׁוְא בִּדְרָכֶךָ חַיֵּנִי׃",
                "הָקֵם לְעַבְדְּךָ אִמְרָתֶךָ אֲשֶׁר לְיִרְאָתֶךָ׃",
                "הַעֲבֵר חֶרְפָּתִי אֲשֶׁר יָגֹרְתִּי כִּי מִשְׁפָּטֶיךָ טוֹבִים׃",
                "הִנֵּה תָּאַבְתִּי לְפִקֻּדֶיךָ בְּצִדְקָתְךָ חַיֵּנִי׃",
                "וִיבֹאֻנִי חֲסָדֶךָ יְהוָה תְּשׁוּעָתְךָ כְּאִמְרָתֶךָ׃",
                "וְאֶעֱנֶה חֹרְפִי דָבָר כִּי־בָטַחְתִּי בִּדְבָרֶךָ׃",
                "וְאַל־תַּצֵּל מִפִּי דְבַר־אֱמֶת עַד־מְאֹד כִּי לְמִשְׁפָּטֶךָ יִחָלְתִּי׃",
                "וְאֶשְׁמְרָה תוֹרָתְךָ תָמִיד לְעוֹלָם וָעֶד׃",
                "וְאֶתְהַלְּכָה בָרְחָבָה כִּי פִקֻּדֶיךָ דָרָשְׁתִּי׃",
                "וַאֲדַבְּרָה בְעֵדֹתֶיךָ נֶגֶד מְלָכִים וְלֹא אֵבוֹשׁ׃",
                "וְאֶשְׁתַּעֲשַׁע בְּמִצְוֺתֶיךָ אֲשֶׁר אָהָבְתִּי׃",
                "וְאֶשָּׂא־כַפַּי אֶל־מִצְוֺתֶיךָ אֲשֶׁר אָהָבְתִּי וְאָשִׂיחָה בְחֻקֶּיךָ׃",
                "זְכֹר־דָּבָר לְעַבְדֶּךָ עַל אֲשֶׁר יִחַלְתָּנִי׃",
                "זֹאת נֶחָמָתִי בְעָנְיִי כִּי אִמְרָתְךָ חִיָּתְנִי׃",
                "זֵדִים הֱלִיצֻנִי עַד־מְאֹד מִתּוֹרָתְךָ לֹא נָטִיתִי׃",
                "זָכַרְתִּי מִשְׁפָּטֶיךָ מֵעוֹלָם יְהוָה וָאֶתְנֶחָם׃",
                "זַלְעָפָה אֲחָזַתְנִי מֵרְשָׁעִים עֹזְבֵי תּוֹרָתֶךָ׃",
                "זְמִרוֹת הָיוּ־לִי חֻקֶּיךָ בְּבֵית מְגוּרָי׃",
                "זָכַרְתִּי בַלַּיְלָה שִׁמְךָ יְהוָה וָאֶשְׁמְרָה תּוֹרָתֶךָ׃",
                "זֹאת הָיְתָה־לִּי כִּי פִקֻּדֶיךָ נָצָרְתִּי׃",
                "חֶלְקִי יְהוָה אָמַרְתִּי לִשְׁמֹר דְּבָרֶיךָ׃",
                "חִלִּיתִי פָנֶיךָ בְכָל־לֵב חָנֵּנִי כְּאִמְרָתֶךָ׃",
                "חִשַּׁבְתִּי דְרָכָי וָאָשִׁיבָה רַגְלַי אֶל־עֵדֹתֶיךָ׃",
                "חַשְׁתִּי וְלֹא הִתְמַהְמָהְתִּי לִשְׁמֹר מִצְוֺתֶיךָ׃",
                "חֶבְלֵי רְשָׁעִים עִוְּדֻנִי תּוֹרָתְךָ לֹא שָׁכָחְתִּי׃",
                "חֲצוֹת־לַיְלָה אָקוּם לְהוֹדוֹת לָךְ עַל מִשְׁפְּטֵי צִדְקֶךָ׃",
                "חָבֵר אָנִי לְכָל־אֲשֶׁר יְרֵאוּךָ וּלְשֹׁמְרֵי פִּקּוּדֶיךָ׃",
                "חַסְדְּךָ יְהוָה מָלְאָה הָאָרֶץ חֻקֶּיךָ לַמְּדֵנִי׃",
                "טוֹב עָשִׂיתָ עִם־עַבְדְּךָ יְהוָה כִּדְבָרֶךָ׃",
                "טוּב טַעַם וָדַעַת לַמְּדֵנִי כִּי בְמִצְוֺתֶיךָ הֶאֱמָנְתִּי׃",
                "טֶרֶם אֶעֱנֶה אֲנִי שֹׁגֵג וְעַתָּה אִמְרָתְךָ שָׁמָרְתִּי׃",
                "טוֹב־אַתָּה וּמֵטִיב לַמְּדֵנִי חֻקֶּיךָ׃",
                "טָפְלוּ עָלַי שֶׁקֶר זֵדִים אֲנִי בְּכָל־לֵב אֱצֹּר פִּקּוּדֶיךָ׃",
                "טָפַשׁ כַּחֵלֶב לִבָּם אֲנִי תּוֹרָתְךָ שִׁעֲשָׁעְתִּי׃",
                "טוֹב־לִי כִי־עֻנֵּיתִי לְמַעַן אֶלְמַד חֻקֶּיךָ׃",
                "טוֹב־לִי תוֹרַת־פִּיךָ מֵאַלְפֵי זָהָב וָכָסֶף׃",
                "יָדֶיךָ עָשׂוּנִי וַיְכוֹנְנוּנִי הֲבִינֵנִי וְאֶלְמְדָה מִצְוֺתֶיךָ׃",
                "יְרֵאֶיךָ יִרְאוּנִי וְיִשְׂמָחוּ כִּי לִדְבָרְךָ יִחָלְתִּי׃",
                "יָדַעְתִּי יְהוָה כִּי־צֶדֶק מִשְׁפָּטֶיךָ וֶאֱמוּנָה עִנִּיתָנִי׃",
                "יְהִי־נָא חַסְדְּךָ לְנַחֲמֵנִי כְּאִמְרָתְךָ לְעַבְדֶּךָ׃",
                "יְבֹאוּנִי רַחֲמֶיךָ וְאֶחְיֶה כִּי־תוֹרָתְךָ שַׁעֲשֻׁעָי׃",
                "יֵבֹשׁוּ זֵדִים כִּי־שֶׁקֶר עִוְּתוּנִי אֲנִי אָשִׂיחַ בְּפִקּוּדֶיךָ׃",
                "יָשׁוּבוּ לִי יְרֵאֶיךָ וידעו [וְיֹדְעֵי] עֵדֹתֶיךָ׃",
                "יְהִי־לִבִּי תָמִים בְּחֻקֶּיךָ לְמַעַן לֹא אֵבוֹשׁ׃",
                "כָּלְתָה לִתְשׁוּעָתְךָ נַפְשִׁי לִדְבָרְךָ יִחָלְתִּי׃",
                "כָּלוּ עֵינַי לְאִמְרָתֶךָ לֵאמֹר מָתַי תְּנַחֲמֵנִי׃",
                "כִּי־הָיִיתִי כְּנֹאד בְּקִיטוֹר חֻקֶּיךָ לֹא שָׁכָחְתִּי׃",
                "כַּמָּה יְמֵי־עַבְדֶּךָ מָתַי תַּעֲשֶׂה בְרֹדְפַי מִשְׁפָּט׃",
                "כָּרוּ־לִי זֵדִים שִׁיחוֹת אֲשֶׁר לֹא כְתוֹרָתֶךָ׃",
                "כָּל־מִצְוֺתֶיךָ אֱמוּנָה שֶׁקֶר רְדָפוּנִי עָזְרֵנִי׃",
                "כִּמְעַט כִּלּוּנִי בָאָרֶץ וַאֲנִי לֹא־עָזַבְתִּי פִקֻּודֶיךָ׃",
                "כְּחַסְדְּךָ חַיֵּנִי וְאֶשְׁמְרָה עֵדוּת פִּיךָ׃",
                "לְעוֹלָם יְהוָה דְּבָרְךָ נִצָּב בַּשָּׁמָיִם׃",
                "לְדֹר וָדֹר אֱמוּנָתֶךָ כּוֹנַנְתָּ אֶרֶץ וַתַּעֲמֹד׃",
                "לְמִשְׁפָּטֶיךָ עָמְדוּ הַיּוֹם כִּי הַכֹּל עֲבָדֶיךָ׃",
                "לוּלֵי תוֹרָתְךָ שַׁעֲשֻׁעָי אָז אָבַדְתִּי בְעָנְיִי׃",
                "לְעוֹלָם לֹא־אֶשְׁכַּח פִּקּוּדֶיךָ כִּי בָם חִיִּיתָנִי׃",
                "לְךָ־אֲנִי הוֹשִׁיעֵנִי כִּי פִקּוּדֶיךָ דָרָשְׁתִּי׃",
                "לִי קִוּוּ רְשָׁעִים לְאַבְּדֵנִי עֵדֹתֶיךָ אֶתְבּוֹנָן׃",
                "לְכָל תִּכְלָה רָאִיתִי קֵץ רְחָבָה מִצְוָתְךָ מְאֹד׃",
                "מָה־אָהַבְתִּי תוֹרָתֶךָ כָּל־הַיּוֹם הִיא שִׂיחָתִי׃",
                "מֵאֹיְבַי תְּחַכְּמֵנִי מִצְוֺתֶךָ כִּי לְעוֹלָם הִיא־לִי׃",
                "מִכָּל־מְלַמְּדַי הִשְׂכַּלְתִּי כִּי עֵדְוֺתֶיךָ שִׂיחָה לִי׃",
                "מִזְּקֵנִים אֶתְבּוֹנָן כִּי פִקּוּדֶיךָ נָצָרְתִּי׃",
                "מִכָּל־אֹרַח רָע כָּלִאתִי רַגְלָי לְמַעַן אֶשְׁמֹר דְּבָרֶךָ׃",
                "מִמִּשְׁפָּטֶיךָ לֹא־סָרְתִּי כִּי־אַתָּה הוֹרֵתָנִי׃",
                "מַה־נִּמְלְצוּ לְחִכִּי אִמְרָתֶךָ מִדְּבַשׁ לְפִי׃",
                "מִפִּקּוּדֶיךָ אֶתְבּוֹנָן עַל־כֵּן שָׂנֵאתִי כָּל־אֹרַח שָׁקֶר׃",
                "נֵר־לְרַגְלִי דְבָרֶךָ וְאוֹר לִנְתִיבָתִי׃",
                "נִשְׁבַּעְתִּי וָאֲקַיֵּמָה לִשְׁמֹר מִשְׁפְּטֵי צִדְקֶךָ׃",
                "נַעֲנֵיתִי עַד־מְאֹד יְהוָה חַיֵּנִי כִדְבָרֶךָ׃",
                "נִדְבוֹת פִּי רְצֵה־נָא יְהוָה וּמִשְׁפָּטֶיךָ לַמְּדֵנִי׃",
                "נַפְשִׁי בְכַפִּי תָמִיד וְתוֹרָתְךָ לֹא שָׁכָחְתִּי׃",
                "נָתְנוּ רְשָׁעִים פַּח לִי וּמִפִּקּוּדֶיךָ לֹא תָעִיתִי׃",
                "נָחַלְתִּי עֵדְוֺתֶיךָ לְעוֹלָם כִּי־שְׂשׂוֹן לִבִּי הֵמָּה׃",
                "נָטִיתִי לִבִּי לַעֲשׂוֹת חֻקֶּיךָ לְעוֹלָם עֵקֶב׃",
                "סֵעֲפִים שָׂנֵאתִי וְתוֹרָתְךָ אָהָבְתִּי׃",
                "סִתְרִי וּמָגִנִּי אָתָּה לִדְבָרְךָ יִחָלְתִּי׃",
                "סוּרוּ־מִמֶּנִּי מְרֵעִים וְאֶצְּרָה מִצְוֺת אֱלֹהָי׃",
                "סָמְכֵנִי כְאִמְרָתְךָ וְאֶחְיֶה וְאַל־תְּבִישֵׁנִי מִשִּׂבְרִי׃",
                "סְעָדֵנִי וְאִוָּשֵׁעָה וְאֶשְׁעָה בְחֻקֶּיךָ תָמִיד׃",
                "סָלִיתָ כָּל־שׁוֹגִים מֵחֻקֶּיךָ כִּי־שֶׁקֶר תַּרְמִיתָם׃",
                "סִגִים הִשְׁבַּתָּ כָל־רִשְׁעֵי־אָרֶץ לָכֵן אָהַבְתִּי עֵדֹתֶיךָ׃",
                "סָמַר מִפַּחְדְּךָ בְשָׂרִי וּמִמִּשְׁפָּטֶיךָ יָרֵאתִי׃",
                "עָשִׂיתִי מִשְׁפָּט וָצֶדֶק בַּל־תַּנִּיחֵנִי לְעֹשְׁקָי׃",
                "עֲרֹב עַבְדְּךָ לְטוֹב אַל־יַעַשְׁקֻנִי זֵדִים׃",
                "עֵינַי כָּלוּ לִישׁוּעָתֶךָ וּלְאִמְרַת צִדְקֶךָ׃",
                "עֲשֵׂה עִם־עַבְדְּךָ כְחַסְדֶּךָ וְחֻקֶּיךָ לַמְּדֵנִי׃",
                "עַבְדְּךָ־אָנִי הֲבִינֵנִי וְאֵדְעָה עֵדֹתֶיךָ׃",
                "עֵת לַעֲשׂוֹת לַיהוָה הֵפֵרוּ תּוֹרָתֶךָ׃",
                "עַל־כֵּן אָהַבְתִּי מִצְוֺתֶיךָ מִזָּהָב וּמִפָּז׃",
                "עַל־כֵּן כָּל־פִּקּוּדֵי כֹל יִשָּׁרְתִּי כָּל־אֹרַח שֶׁקֶר שָׂנֵאתִי׃",
                "פְּלָאוֹת עֵדְוֺתֶיךָ עַל־כֵּן נְצָרָתַם נַפְשִׁי׃",
                "פֵּתַח דְּבָרֶיךָ יָאִיר מֵבִין פְּתָיִים׃",
                "פִּי־פָעַרְתִּי וָאֶשְׁאָפָה כִּי לְמִצְוֺתֶיךָ יָאָבְתִּי׃",
                "פְּנֵה־אֵלַי וְחָנֵּנִי כְּמִשְׁפָּט לְאֹהֲבֵי שְׁמֶךָ׃",
                "פְּעָמַי הָכֵן בְּאִמְרָתֶךָ וְאַל־תַּשְׁלֶט־בִּי כָל־אָוֶן׃",
                "פְּדֵנִי מֵעֹשֶׁק אָדָם וְאֶשְׁמְרָה פִּקּוּדֶיךָ׃",
                "פָּנֶיךָ הָאֵר בְּעַבְדֶּךָ וְלַמְּדֵנִי אֶת־חֻקֶּיךָ׃",
                "פַּלְגֵי־מַיִם יָרְדוּ עֵינָי עַל לֹא־שָׁמְרוּ תוֹרָתֶךָ׃",
                "צַדִּיק אַתָּה יְהוָה וְיָשָׁר מִשְׁפָּטֶיךָ׃",
                "צִוִּיתָ צֶדֶק עֵדֹתֶיךָ וֶאֱמוּנָה מְאֹד׃",
                "צִמְּתַתְנִי קִנְאָתִי כִּי־שָׁכְחוּ דְבָרֶיךָ צָרָי׃",
                "צְרוּפָה אִמְרָתְךָ מְאֹד וְעַבְדְּךָ אֲהֵבָהּ׃",
                "צָעִיר אָנֹכִי וְנִבְזֶה פִּקֻּדֶיךָ לֹא שָׁכָחְתִּי׃",
                "צִדְקָתְךָ צֶדֶק לְעוֹלָם וְתוֹרָתְךָ אֱמֶת׃",
                "צַר־וּמָצוֹק מְצָאוּנִי מִצְוֺתֶיךָ שַׁעֲשֻׁעָי׃",
                "צֶדֶק עֵדְוֺתֶיךָ לְעוֹלָם הֲבִינֵנִי וְאֶחְיֶה׃",
                "קָרָאתִי בְכָל־לֵב עֲנֵנִי יְהוָה חֻקֶּיךָ אֶצֹּרָה׃",
                "קְרָאתִיךָ הוֹשִׁיעֵנִי וְאֶשְׁמְרָה עֵדֹתֶיךָ׃",
                "קִדַּמְתִּי בַנֶּשֶׁף וָאֲשַׁוֵּעָה לדבריך [לִדְבָרְךָ] יִחָלְתִּי׃",
                "קִדְּמוּ עֵינַי אַשְׁמֻרוֹת לָשִׂיחַ בְּאִמְרָתֶךָ׃",
                "קוֹלִי שִׁמְעָה כְחַסְדֶּךָ יְהוָה כְּמִשְׁפָּטֶךָ חַיֵּנִי׃",
                "קָרְבוּ רֹדְפֵי זִמָּה מִתּוֹרָתְךָ רָחָקוּ׃",
                "קָרוֹב אַתָּה יְהוָה וְכָל־מִצְוֺתֶיךָ אֱמֶת׃",
                "קֶדֶם יָדַעְתִּי מֵעֵדֹתֶיךָ כִּי לְעוֹלָם יְסַדְתָּם׃",
                "רְאֵה־עָנְיִי וְחַלְּצֵנִי כִּי־תוֹרָתְךָ לֹא שָׁכָחְתִּי׃",
                "רִיבָה רִיבִי וּגְאָלֵנִי לְאִמְרָתְךָ חַיֵּנִי׃",
                "רָחוֹק מֵרְשָׁעִים יְשׁוּעָה כִּי־חֻקֶּיךָ לֹא דָרָשׁוּ׃",
                "רַחֲמֶיךָ רַבִּים יְהוָה כְּמִשְׁפָּטֶיךָ חַיֵּנִי׃",
                "רַבִּים רֹדְפַי וְצָרָי מֵעֵדְוֺתֶיךָ לֹא נָטִיתִי׃",
                "רָאִיתִי בֹגְדִים וָאֶתְקוֹטָטָה אֲשֶׁר אִמְרָתְךָ לֹא שָׁמָרוּ׃",
                "רְאֵה כִּי־פִקּוּדֶיךָ אָהָבְתִּי יְהוָה כְּחַסְדְּךָ חַיֵּנִי׃",
                "רֹאשׁ־דְּבָרְךָ אֱמֶת וּלְעוֹלָם כָּל־מִשְׁפַּט צִדְקֶךָ׃",
                "שָׂרִים רְדָפוּנִי חִנָּם ומדבריך [וּמִדְּבָרְךָ] פָּחַד לִבִּי׃",
                "שָׂשׂ אָנֹכִי עַל־אִמְרָתֶךָ כְּמוֹצֵא שָׁלָל רָב׃",
                "שֶׁקֶר שָׂנֵאתִי וַאֲתַעֵבָה תּוֹרָתְךָ אָהָבְתִּי׃",
                "שֶׁבַע בַּיּוֹם הִלַּלְתִּיךָ עַל מִשְׁפְּטֵי צִדְקֶךָ׃",
                "שָׁלוֹם רָב לְאֹהֲבֵי תוֹרָתֶךָ וְאֵין־לָמוֹ מִכְשׁוֹל׃",
                "שִׂבַּרְתִּי לִישׁוּעָתְךָ יְהוָה וּמִצְוֺתֶיךָ עָשִׂיתִי׃",
                "שָׁמְרָה נַפְשִׁי עֵדֹתֶיךָ וָאֹהֲבֵם מְאֹד׃",
                "שָׁמַרְתִּי פִקּוּדֶיךָ וְעֵדֹתֶיךָ כִּי כָל־דְּרָכַי נֶגְדֶּךָ׃",
                "תִּקְרַב רִנָּתִי לְפָנֶיךָ יְהוָה כִּדְבָרְךָ הֲבִינֵנִי׃",
                "תָּבוֹא תְּחִנָּתִי לְפָנֶיךָ כְּאִמְרָתְךָ הַצִּילֵנִי׃",
                "תַּבַּעְנָה שְׂפָתַי תְּהִלָּה כִּי תְלַמְּדֵנִי חֻקֶּיךָ׃",
                "תַּעַן לְשׁוֹנִי אִמְרָתֶךָ כִּי כָל־מִצְוֺתֶיךָ צֶּדֶק׃",
                "תְּהִי־יָדְךָ לְעָזְרֵנִי כִּי פִקּוּדֶיךָ בָחָרְתִּי׃",
                "תָּאַבְתִּי לִישׁוּעָתְךָ יְהוָה וְתוֹרָתְךָ שַׁעֲשֻׁעָי׃",
                "תְּחִי־נַפְשִׁי וּתְהַלְלֶךָּ וּמִשְׁפָּטֶךָ יַעֲזְרֻנִי׃",
                "תָּעִיתִי כְּשֶׂה אֹבֵד בַּקֵּשׁ עַבְדֶּךָ כִּי מִצְוֺתֶיךָ לֹא שָׁכָחְתִּי׃"
            ]

    Users = Bot_Variables[10][0]
    Chat_ID = Bot_Variables[1]


    text = ""

    if letter == "ם":
        letter = "מ"

    if letter == "ן":
        letter = "נ"

    if letter == "ץ":
        letter = "צ"

    if letter == "ף":
        letter = "פ"

    if letter == "ך":
        letter = "כ"

    for i in range(len(neshama)):

        if neshama[i][0] == letter:
            text = text + neshama[i] + "\n"


    place = str(Users.find_one({"chat_id":Chat_ID})["neshama"]["place"] + 1)

    letter = "אות: {} ({}) ".format(letter,place) + " "
    name = Users.find_one({"chat_id":Chat_ID})["neshama"]["name"]



    letter = letter +  "מתוך ({})".format(name) + "\n\n"
    return letter + text


#print(Func("א"))