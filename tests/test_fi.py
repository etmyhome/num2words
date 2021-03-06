# -*- coding: utf-8 -*-
# Copyright (c) 2003, Taro Ogawa.  All Rights Reserved.
# Copyright (c) 2013, Savoir-faire Linux inc.  All Rights Reserved.

# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# Lesser General Public License for more details.
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
# MA 02110-1301 USA

from __future__ import division, print_function, unicode_literals

from unittest import TestCase

from num2words import num2words

CASES = ["nominative", "genitive", "partitive",    # grammatical
         "inessive", "elative", "illative",        # internal locative
         "adessive", "ablative", "allative",       # external locative
         "essive", "translative",                  # essive
         "instructive", "abessive", "comitative"]  # rare


def n2f(*args, **kwargs):
    return num2words(lang='fi', *args, **kwargs)


class Num2WordsFITest(TestCase):

    def test_low(self):

        # zero
        self.assertEqual(
            tuple(n2f(0, to="cardinal", case=c) for c in CASES),
            ("nolla", "nollan", "nollaa",
             "nollassa", "nollasta", "nollaan",
             "nollalla", "nollalta", "nollalle",
             "nollana", "nollaksi",
             "nollin", "nollatta", "nolline")
        )
        self.assertEqual(
            tuple(n2f(0, to="cardinal", case=c, plural=True) for c in CASES),
            ("nollat", "nollien", "nollia",
             "nollissa", "nollista", "nolliin",
             "nollilla", "nollilta", "nollille",
             "nollina", "nolliksi",
             "nollin", "nollitta", "nolline")
        )

        # one
        self.assertEqual(
            tuple(n2f(1, to="cardinal", case=c) for c in CASES),
            ("yksi", "yhden", "yht??",
             "yhdess??", "yhdest??", "yhteen",
             "yhdell??", "yhdelt??", "yhdelle",
             "yhten??", "yhdeksi",
             "yksin", "yhdett??", "yksine")
        )
        self.assertEqual(
            tuple(n2f(1, to="cardinal", case=c, plural=True) for c in CASES),
            ("yhdet", "yksien", "yksi??",
             "yksiss??", "yksist??", "yksiin",
             "yksill??", "yksilt??", "yksille",
             "yksin??", "yksiksi",
             "yksin", "yksitt??", "yksine")
        )

        # two
        self.assertEqual(
            tuple(n2f(2, to="cardinal", case=c) for c in CASES),
            ("kaksi", "kahden", "kahta",
             "kahdessa", "kahdesta", "kahteen",
             "kahdella", "kahdelta", "kahdelle",
             "kahtena", "kahdeksi",
             "kaksin", "kahdetta", "kaksine")
        )
        self.assertEqual(
            tuple(n2f(2, to="cardinal", case=c, plural=True) for c in CASES),
            ("kahdet", "kaksien", "kaksia",
             "kaksissa", "kaksista", "kaksiin",
             "kaksilla", "kaksilta", "kaksille",
             "kaksina", "kaksiksi",
             "kaksin", "kaksitta", "kaksine")
        )

        # three
        self.assertEqual(
            tuple(n2f(3, to="cardinal", case=c) for c in CASES),
            ("kolme", "kolmen", "kolmea",
             "kolmessa", "kolmesta", "kolmeen",
             "kolmella", "kolmelta", "kolmelle",
             "kolmena", "kolmeksi",
             "kolmen", "kolmetta", "kolmine")
        )
        self.assertEqual(
            tuple(n2f(3, to="cardinal", case=c, plural=True) for c in CASES),
            ("kolmet", "kolmien", "kolmia",
             "kolmissa", "kolmista", "kolmiin",
             "kolmilla", "kolmilta", "kolmille",
             "kolmina", "kolmiksi",
             "kolmin", "kolmitta", "kolmine")
        )

        # four
        self.assertEqual(
            tuple(n2f(4, to="cardinal", case=c) for c in CASES),
            ("nelj??", "nelj??n", "nelj????",
             "nelj??ss??", "nelj??st??", "nelj????n",
             "nelj??ll??", "nelj??lt??", "nelj??lle",
             "nelj??n??", "nelj??ksi",
             "neljin", "nelj??tt??", "neljine")
        )
        self.assertEqual(
            tuple(n2f(4, to="cardinal", case=c, plural=True) for c in CASES),
            ("nelj??t", "neljien", "nelji??",
             "neljiss??", "neljist??", "neljiin",
             "neljill??", "neljilt??", "neljille",
             "neljin??", "neljiksi",
             "neljin", "neljitt??", "neljine")
        )

        # five
        self.assertEqual(
            tuple(n2f(5, to="cardinal", case=c) for c in CASES),
            ("viisi", "viiden", "viitt??",
             "viidess??", "viidest??", "viiteen",
             "viidell??", "viidelt??", "viidelle",
             "viiten??", "viideksi",
             "viisin", "viidett??", "viisine")
        )
        self.assertEqual(
            tuple(n2f(5, to="cardinal", case=c, plural=True) for c in CASES),
            ("viidet", "viisien", "viisi??",
             "viisiss??", "viisist??", "viisiin",
             "viisill??", "viisilt??", "viisille",
             "viisin??", "viisiksi",
             "viisin", "viisitt??", "viisine")
        )

        # six
        self.assertEqual(
            tuple(n2f(6, to="cardinal", case=c) for c in CASES),
            ("kuusi", "kuuden", "kuutta",
             "kuudessa", "kuudesta", "kuuteen",
             "kuudella", "kuudelta", "kuudelle",
             "kuutena", "kuudeksi",
             "kuusin", "kuudetta", "kuusine")
        )
        self.assertEqual(
            tuple(n2f(6, to="cardinal", case=c, plural=True) for c in CASES),
            ("kuudet", "kuusien", "kuusia",
             "kuusissa", "kuusista", "kuusiin",
             "kuusilla", "kuusilta", "kuusille",
             "kuusina", "kuusiksi",
             "kuusin", "kuusitta", "kuusine")
        )

        # seven
        self.assertEqual(
            tuple(n2f(7, to="cardinal", case=c) for c in CASES),
            ("seitsem??n", "seitsem??n", "seitsem????",
             "seitsem??ss??", "seitsem??st??", "seitsem????n",
             "seitsem??ll??", "seitsem??lt??", "seitsem??lle",
             "seitsem??n??", "seitsem??ksi",
             "seitsemin", "seitsem??tt??", "seitsemine")
        )
        self.assertEqual(
            tuple(n2f(7, to="cardinal", case=c, plural=True) for c in CASES),
            ("seitsem??t", "seitsemien", "seitsemi??",
             "seitsemiss??", "seitsemist??", "seitsemiin",
             "seitsemill??", "seitsemilt??", "seitsemille",
             "seitsemin??", "seitsemiksi",
             "seitsemin", "seitsemitt??", "seitsemine")
        )

        # eight
        self.assertEqual(
            tuple(n2f(8, to="cardinal", case=c) for c in CASES),
            ("kahdeksan", "kahdeksan", "kahdeksaa",
             "kahdeksassa", "kahdeksasta", "kahdeksaan",
             "kahdeksalla", "kahdeksalta", "kahdeksalle",
             "kahdeksana", "kahdeksaksi",
             "kahdeksin", "kahdeksatta", "kahdeksine")
        )
        self.assertEqual(
            tuple(n2f(8, to="cardinal", case=c, plural=True) for c in CASES),
            ("kahdeksat", "kahdeksien", "kahdeksia",
             "kahdeksissa", "kahdeksista", "kahdeksiin",
             "kahdeksilla", "kahdeksilta", "kahdeksille",
             "kahdeksina", "kahdeksiksi",
             "kahdeksin", "kahdeksitta", "kahdeksine")
        )
        self.assertEqual(
            n2f(8, to="cardinal", case="genitive", plural=True,
                prefer=["ain"]),
            "kahdeksain"
        )

        # nine
        self.assertEqual(
            tuple(n2f(9, to="cardinal", case=c) for c in CASES),
            ("yhdeks??n", "yhdeks??n", "yhdeks????",
             "yhdeks??ss??", "yhdeks??st??", "yhdeks????n",
             "yhdeks??ll??", "yhdeks??lt??", "yhdeks??lle",
             "yhdeks??n??", "yhdeks??ksi",
             "yhdeksin", "yhdeks??tt??", "yhdeksine")
        )
        self.assertEqual(
            tuple(n2f(9, to="cardinal", case=c, plural=True) for c in CASES),
            ("yhdeks??t", "yhdeksien", "yhdeksi??",
             "yhdeksiss??", "yhdeksist??", "yhdeksiin",
             "yhdeksill??", "yhdeksilt??", "yhdeksille",
             "yhdeksin??", "yhdeksiksi",
             "yhdeksin", "yhdeksitt??", "yhdeksine")
        )

        # ten
        self.assertEqual(
            tuple(n2f(10, to="cardinal", case=c) for c in CASES),
            ("kymmenen", "kymmenen", "kymment??",
             "kymmeness??", "kymmenest??", "kymmeneen",
             "kymmenell??", "kymmenelt??", "kymmenelle",
             "kymmenen??", "kymmeneksi",
             "kymmenin", "kymmenett??", "kymmenine")
        )
        self.assertEqual(
            tuple(n2f(10, to="cardinal", case=c, plural=True) for c in CASES),
            ("kymmenet", "kymmenien", "kymmeni??",
             "kymmeniss??", "kymmenist??", "kymmeniin",
             "kymmenill??", "kymmenilt??", "kymmenille",
             "kymmenin??", "kymmeniksi",
             "kymmenin", "kymmenitt??", "kymmenine")
        )

        # eleven
        self.assertEqual(
            tuple(n2f(11, to="cardinal", case=c) for c in CASES),
            ("yksitoista", "yhdentoista", "yht??toista",
             "yhdess??toista", "yhdest??toista", "yhteentoista",
             "yhdell??toista", "yhdelt??toista", "yhdelletoista",
             "yhten??toista", "yhdeksitoista",
             "yksintoista", "yhdett??toista", "yksinetoista")
        )
        self.assertEqual(
            tuple(n2f(11, to="cardinal", case=c, plural=True) for c in CASES),
            ("yhdettoista", "yksientoista", "yksi??toista",
             "yksiss??toista", "yksist??toista", "yksiintoista",
             "yksill??toista", "yksilt??toista", "yksilletoista",
             "yksin??toista", "yksiksitoista",
             "yksintoista", "yksitt??toista", "yksinetoista")
        )

        # twelve
        self.assertEqual(
            tuple(n2f(12, to="cardinal", case=c) for c in CASES),
            ("kaksitoista", "kahdentoista", "kahtatoista",
             "kahdessatoista", "kahdestatoista", "kahteentoista",
             "kahdellatoista", "kahdeltatoista", "kahdelletoista",
             "kahtenatoista", "kahdeksitoista",
             "kaksintoista", "kahdettatoista", "kaksinetoista")
        )
        self.assertEqual(
            tuple(n2f(12, to="cardinal", case=c, plural=True) for c in CASES),
            ("kahdettoista", "kaksientoista", "kaksiatoista",
             "kaksissatoista", "kaksistatoista", "kaksiintoista",
             "kaksillatoista", "kaksiltatoista", "kaksilletoista",
             "kaksinatoista", "kaksiksitoista",
             "kaksintoista", "kaksittatoista", "kaksinetoista")
        )

        # thirteen
        self.assertEqual(
            tuple(n2f(13, to="cardinal", case=c) for c in CASES),
            ("kolmetoista", "kolmentoista", "kolmeatoista",
             "kolmessatoista", "kolmestatoista", "kolmeentoista",
             "kolmellatoista", "kolmeltatoista", "kolmelletoista",
             "kolmenatoista", "kolmeksitoista",
             "kolmentoista", "kolmettatoista", "kolminetoista")
        )
        self.assertEqual(
            tuple(n2f(13, to="cardinal", case=c, plural=True) for c in CASES),
            ("kolmettoista", "kolmientoista", "kolmiatoista",
             "kolmissatoista", "kolmistatoista", "kolmiintoista",
             "kolmillatoista", "kolmiltatoista", "kolmilletoista",
             "kolminatoista", "kolmiksitoista",
             "kolmintoista", "kolmittatoista", "kolminetoista")
        )

        # fourteen
        self.assertEqual(
            tuple(n2f(14, to="cardinal", case=c) for c in CASES),
            ("nelj??toista", "nelj??ntoista", "nelj????toista",
             "nelj??ss??toista", "nelj??st??toista", "nelj????ntoista",
             "nelj??ll??toista", "nelj??lt??toista", "nelj??lletoista",
             "nelj??n??toista", "nelj??ksitoista",
             "neljintoista", "nelj??tt??toista", "neljinetoista")
        )
        self.assertEqual(
            tuple(n2f(14, to="cardinal", case=c, plural=True) for c in CASES),
            ("nelj??ttoista", "neljientoista", "nelji??toista",
             "neljiss??toista", "neljist??toista", "neljiintoista",
             "neljill??toista", "neljilt??toista", "neljilletoista",
             "neljin??toista", "neljiksitoista",
             "neljintoista", "neljitt??toista", "neljinetoista")
        )

        # fifteen
        self.assertEqual(
            tuple(n2f(15, to="cardinal", case=c) for c in CASES),
            ("viisitoista", "viidentoista", "viitt??toista",
             "viidess??toista", "viidest??toista", "viiteentoista",
             "viidell??toista", "viidelt??toista", "viidelletoista",
             "viiten??toista", "viideksitoista",
             "viisintoista", "viidett??toista", "viisinetoista")
        )
        self.assertEqual(
            tuple(n2f(15, to="cardinal", case=c, plural=True) for c in CASES),
            ("viidettoista", "viisientoista", "viisi??toista",
             "viisiss??toista", "viisist??toista", "viisiintoista",
             "viisill??toista", "viisilt??toista", "viisilletoista",
             "viisin??toista", "viisiksitoista",
             "viisintoista", "viisitt??toista", "viisinetoista")
        )

        # sixteen
        self.assertEqual(
            tuple(n2f(16, to="cardinal", case=c) for c in CASES),
            ("kuusitoista", "kuudentoista", "kuuttatoista",
             "kuudessatoista", "kuudestatoista", "kuuteentoista",
             "kuudellatoista", "kuudeltatoista", "kuudelletoista",
             "kuutenatoista", "kuudeksitoista",
             "kuusintoista", "kuudettatoista", "kuusinetoista")
        )
        self.assertEqual(
            tuple(n2f(16, to="cardinal", case=c, plural=True) for c in CASES),
            ("kuudettoista", "kuusientoista", "kuusiatoista",
             "kuusissatoista", "kuusistatoista", "kuusiintoista",
             "kuusillatoista", "kuusiltatoista", "kuusilletoista",
             "kuusinatoista", "kuusiksitoista",
             "kuusintoista", "kuusittatoista", "kuusinetoista")
        )

        # seventeen
        self.assertEqual(
            tuple(n2f(17, to="cardinal", case=c) for c in CASES),
            ("seitsem??ntoista", "seitsem??ntoista", "seitsem????toista",
             "seitsem??ss??toista", "seitsem??st??toista", "seitsem????ntoista",
             "seitsem??ll??toista", "seitsem??lt??toista", "seitsem??lletoista",
             "seitsem??n??toista", "seitsem??ksitoista",
             "seitsemintoista", "seitsem??tt??toista", "seitseminetoista")
        )
        self.assertEqual(
            tuple(n2f(17, to="cardinal", case=c, plural=True) for c in CASES),
            ("seitsem??ttoista", "seitsemientoista", "seitsemi??toista",
             "seitsemiss??toista", "seitsemist??toista", "seitsemiintoista",
             "seitsemill??toista", "seitsemilt??toista", "seitsemilletoista",
             "seitsemin??toista", "seitsemiksitoista",
             "seitsemintoista", "seitsemitt??toista", "seitseminetoista")
        )

        # eighteen
        self.assertEqual(
            tuple(n2f(18, to="cardinal", case=c) for c in CASES),
            ("kahdeksantoista", "kahdeksantoista", "kahdeksaatoista",
             "kahdeksassatoista", "kahdeksastatoista", "kahdeksaantoista",
             "kahdeksallatoista", "kahdeksaltatoista", "kahdeksalletoista",
             "kahdeksanatoista", "kahdeksaksitoista",
             "kahdeksintoista", "kahdeksattatoista", "kahdeksinetoista")
        )
        self.assertEqual(
            tuple(n2f(18, to="cardinal", case=c, plural=True) for c in CASES),
            ("kahdeksattoista", "kahdeksientoista", "kahdeksiatoista",
             "kahdeksissatoista", "kahdeksistatoista", "kahdeksiintoista",
             "kahdeksillatoista", "kahdeksiltatoista", "kahdeksilletoista",
             "kahdeksinatoista", "kahdeksiksitoista",
             "kahdeksintoista", "kahdeksittatoista", "kahdeksinetoista")
        )

        # nineteen
        self.assertEqual(
            tuple(n2f(19, to="cardinal", case=c) for c in CASES),
            ("yhdeks??ntoista", "yhdeks??ntoista", "yhdeks????toista",
             "yhdeks??ss??toista", "yhdeks??st??toista", "yhdeks????ntoista",
             "yhdeks??ll??toista", "yhdeks??lt??toista", "yhdeks??lletoista",
             "yhdeks??n??toista", "yhdeks??ksitoista",
             "yhdeksintoista", "yhdeks??tt??toista", "yhdeksinetoista")
        )
        self.assertEqual(
            tuple(n2f(19, to="cardinal", case=c, plural=True) for c in CASES),
            ("yhdeks??ttoista", "yhdeksientoista", "yhdeksi??toista",
             "yhdeksiss??toista", "yhdeksist??toista", "yhdeksiintoista",
             "yhdeksill??toista", "yhdeksilt??toista", "yhdeksilletoista",
             "yhdeksin??toista", "yhdeksiksitoista",
             "yhdeksintoista", "yhdeksitt??toista", "yhdeksinetoista")
        )

        # twenty
        self.assertEqual(
            tuple(n2f(20, to="cardinal", case=c) for c in CASES),
            ("kaksikymment??", "kahdenkymmenen", "kahtakymment??",
             "kahdessakymmeness??", "kahdestakymmenest??", "kahteenkymmeneen",
             "kahdellakymmenell??", "kahdeltakymmenelt??", "kahdellekymmenelle",
             "kahtenakymmenen??", "kahdeksikymmeneksi",
             "kaksinkymmenin", "kahdettakymmenett??", "kaksinekymmenine")
        )
        self.assertEqual(
            tuple(n2f(20, to="cardinal", case=c, plural=True) for c in CASES),
            ("kahdetkymmenet", "kaksienkymmenien", "kaksiakymmeni??",
             "kaksissakymmeniss??", "kaksistakymmenist??", "kaksiinkymmeniin",
             "kaksillakymmenill??", "kaksiltakymmenilt??", "kaksillekymmenille",
             "kaksinakymmenin??", "kaksiksikymmeniksi",
             "kaksinkymmenin", "kaksittakymmenitt??", "kaksinekymmenine")
        )

    def test_low_ord(self):

        # minus one
        with self.assertRaises(TypeError):
            n2f(-1, to="ordinal")

        # zero
        self.assertEqual(
            tuple(n2f(0, to="ordinal", case=c) for c in CASES),
            ("nollas", "nollannen", "nollatta",
             "nollannessa", "nollannesta", "nollanteen",
             "nollannella", "nollannelta", "nollannelle",
             "nollantena", "nollanneksi",
             "nollansin", "nollannetta", "nollansine")
        )
        self.assertEqual(
            tuple(n2f(0, to="ordinal", case=c, plural=True) for c in CASES),
            ("nollannet", "nollansien", "nollansia",
             "nollansissa", "nollansista", "nollansiin",
             "nollansilla", "nollansilta", "nollansille",
             "nollansina", "nollansiksi",
             "nollansin", "nollansitta", "nollansine")
        )

        # one
        self.assertEqual(
            tuple(n2f(1, to="ordinal", case=c) for c in CASES),
            ("ensimm??inen", "ensimm??isen", "ensimm??ist??",
             "ensimm??isess??", "ensimm??isest??", "ensimm??iseen",
             "ensimm??isell??", "ensimm??iselt??", "ensimm??iselle",
             "ensimm??isen??", "ensimm??iseksi",
             "ensimm??isin", "ensimm??isett??", "ensimm??isine")
        )
        self.assertEqual(
            tuple(n2f(1, to="ordinal", case=c, plural=True) for c in CASES),
            ("ensimm??iset", "ensimm??isten", "ensimm??isi??",
             "ensimm??isiss??", "ensimm??isist??", "ensimm??isiin",
             "ensimm??isill??", "ensimm??isilt??", "ensimm??isille",
             "ensimm??isin??", "ensimm??isiksi",
             "ensimm??isin", "ensimm??isitt??", "ensimm??isine")
        )

        # two
        self.assertEqual(
            tuple(n2f(2, to="ordinal", case=c) for c in CASES),
            ("toinen", "toisen", "toista",
             "toisessa", "toisesta", "toiseen",
             "toisella", "toiselta", "toiselle",
             "toisena", "toiseksi",
             "toisin", "toisetta", "toisine")
        )
        self.assertEqual(
            tuple(n2f(2, to="ordinal", case=c, plural=True) for c in CASES),
            ("toiset", "toisten", "toisia",
             "toisissa", "toisista", "toisiin",
             "toisilla", "toisilta", "toisille",
             "toisina", "toisiksi",
             "toisin", "toisitta", "toisine")
        )

        # three
        self.assertEqual(
            tuple(n2f(3, to="ordinal", case=c) for c in CASES),
            ("kolmas", "kolmannen", "kolmatta",
             "kolmannessa", "kolmannesta", "kolmanteen",
             "kolmannella", "kolmannelta", "kolmannelle",
             "kolmantena", "kolmanneksi",
             "kolmansin", "kolmannetta", "kolmansine")
        )
        self.assertEqual(
            tuple(n2f(3, to="ordinal", case=c, plural=True) for c in CASES),
            ("kolmannet", "kolmansien", "kolmansia",
             "kolmansissa", "kolmansista", "kolmansiin",
             "kolmansilla", "kolmansilta", "kolmansille",
             "kolmansina", "kolmansiksi",
             "kolmansin", "kolmansitta", "kolmansine")
        )

        # four
        self.assertEqual(
            tuple(n2f(4, to="ordinal", case=c) for c in CASES),
            ("nelj??s", "nelj??nnen", "nelj??tt??",
             "nelj??nness??", "nelj??nnest??", "nelj??nteen",
             "nelj??nnell??", "nelj??nnelt??", "nelj??nnelle",
             "nelj??nten??", "nelj??nneksi",
             "nelj??nsin", "nelj??nnett??", "nelj??nsine")
        )
        self.assertEqual(
            tuple(n2f(4, to="ordinal", case=c, plural=True) for c in CASES),
            ("nelj??nnet", "nelj??nsien", "nelj??nsi??",
             "nelj??nsiss??", "nelj??nsist??", "nelj??nsiin",
             "nelj??nsill??", "nelj??nsilt??", "nelj??nsille",
             "nelj??nsin??", "nelj??nsiksi",
             "nelj??nsin", "nelj??nsitt??", "nelj??nsine")
        )

        # five
        self.assertEqual(
            tuple(n2f(5, to="ordinal", case=c) for c in CASES),
            ("viides", "viidennen", "viidett??",
             "viidenness??", "viidennest??", "viidenteen",
             "viidennell??", "viidennelt??", "viidennelle",
             "viidenten??", "viidenneksi",
             "viidensin", "viidennett??", "viidensine")
        )
        self.assertEqual(
            tuple(n2f(5, to="ordinal", case=c, plural=True) for c in CASES),
            ("viidennet", "viidensien", "viidensi??",
             "viidensiss??", "viidensist??", "viidensiin",
             "viidensill??", "viidensilt??", "viidensille",
             "viidensin??", "viidensiksi",
             "viidensin", "viidensitt??", "viidensine")
        )

        # six
        self.assertEqual(
            tuple(n2f(6, to="ordinal", case=c) for c in CASES),
            ("kuudes", "kuudennen", "kuudetta",
             "kuudennessa", "kuudennesta", "kuudenteen",
             "kuudennella", "kuudennelta", "kuudennelle",
             "kuudentena", "kuudenneksi",
             "kuudensin", "kuudennetta", "kuudensine")
        )
        self.assertEqual(
            tuple(n2f(6, to="ordinal", case=c, plural=True) for c in CASES),
            ("kuudennet", "kuudensien", "kuudensia",
             "kuudensissa", "kuudensista", "kuudensiin",
             "kuudensilla", "kuudensilta", "kuudensille",
             "kuudensina", "kuudensiksi",
             "kuudensin", "kuudensitta", "kuudensine")
        )

        # seven
        self.assertEqual(
            tuple(n2f(7, to="ordinal", case=c) for c in CASES),
            ("seitsem??s", "seitsem??nnen", "seitsem??tt??",
             "seitsem??nness??", "seitsem??nnest??", "seitsem??nteen",
             "seitsem??nnell??", "seitsem??nnelt??", "seitsem??nnelle",
             "seitsem??nten??", "seitsem??nneksi",
             "seitsem??nsin", "seitsem??nnett??", "seitsem??nsine")
        )
        self.assertEqual(
            tuple(n2f(7, to="ordinal", case=c, plural=True) for c in CASES),
            ("seitsem??nnet", "seitsem??nsien", "seitsem??nsi??",
             "seitsem??nsiss??", "seitsem??nsist??", "seitsem??nsiin",
             "seitsem??nsill??", "seitsem??nsilt??", "seitsem??nsille",
             "seitsem??nsin??", "seitsem??nsiksi",
             "seitsem??nsin", "seitsem??nsitt??", "seitsem??nsine")
        )

        # eight
        self.assertEqual(
            tuple(n2f(8, to="ordinal", case=c) for c in CASES),
            ("kahdeksas", "kahdeksannen", "kahdeksatta",
             "kahdeksannessa", "kahdeksannesta", "kahdeksanteen",
             "kahdeksannella", "kahdeksannelta", "kahdeksannelle",
             "kahdeksantena", "kahdeksanneksi",
             "kahdeksansin", "kahdeksannetta", "kahdeksansine")
        )
        self.assertEqual(
            tuple(n2f(8, to="ordinal", case=c, plural=True) for c in CASES),
            ("kahdeksannet", "kahdeksansien", "kahdeksansia",
             "kahdeksansissa", "kahdeksansista", "kahdeksansiin",
             "kahdeksansilla", "kahdeksansilta", "kahdeksansille",
             "kahdeksansina", "kahdeksansiksi",
             "kahdeksansin", "kahdeksansitta", "kahdeksansine")
        )

        # nine
        self.assertEqual(
            tuple(n2f(9, to="ordinal", case=c) for c in CASES),
            ("yhdeks??s", "yhdeks??nnen", "yhdeks??tt??",
             "yhdeks??nness??", "yhdeks??nnest??", "yhdeks??nteen",
             "yhdeks??nnell??", "yhdeks??nnelt??", "yhdeks??nnelle",
             "yhdeks??nten??", "yhdeks??nneksi",
             "yhdeks??nsin", "yhdeks??nnett??", "yhdeks??nsine")
        )
        self.assertEqual(
            tuple(n2f(9, to="ordinal", case=c, plural=True) for c in CASES),
            ("yhdeks??nnet", "yhdeks??nsien", "yhdeks??nsi??",
             "yhdeks??nsiss??", "yhdeks??nsist??", "yhdeks??nsiin",
             "yhdeks??nsill??", "yhdeks??nsilt??", "yhdeks??nsille",
             "yhdeks??nsin??", "yhdeks??nsiksi",
             "yhdeks??nsin", "yhdeks??nsitt??", "yhdeks??nsine")
        )

        # ten
        self.assertEqual(
            tuple(n2f(10, to="ordinal", case=c) for c in CASES),
            ("kymmenes", "kymmenennen", "kymmenett??",
             "kymmenenness??", "kymmenennest??", "kymmenenteen",
             "kymmenennell??", "kymmenennelt??", "kymmenennelle",
             "kymmenenten??", "kymmenenneksi",
             "kymmenensin", "kymmenennett??", "kymmenensine")
        )
        self.assertEqual(
            tuple(n2f(10, to="ordinal", case=c, plural=True) for c in CASES),
            ("kymmenennet", "kymmenensien", "kymmenensi??",
             "kymmenensiss??", "kymmenensist??", "kymmenensiin",
             "kymmenensill??", "kymmenensilt??", "kymmenensille",
             "kymmenensin??", "kymmenensiksi",
             "kymmenensin", "kymmenensitt??", "kymmenensine")
        )

        # eleven
        self.assertEqual(
            tuple(n2f(11, to="ordinal", case=c) for c in CASES),
            ("yhdestoista", "yhdennentoista", "yhdett??toista",
             "yhdenness??toista", "yhdennest??toista", "yhdenteentoista",
             "yhdennell??toista", "yhdennelt??toista", "yhdennelletoista",
             "yhdenten??toista", "yhdenneksitoista",
             "yhdensintoista", "yhdennett??toista", "yhdensinetoista")
        )
        self.assertEqual(
            tuple(n2f(11, to="ordinal", case=c, plural=True) for c in CASES),
            ("yhdennettoista", "yhdensientoista", "yhdensi??toista",
             "yhdensiss??toista", "yhdensist??toista", "yhdensiintoista",
             "yhdensill??toista", "yhdensilt??toista", "yhdensilletoista",
             "yhdensin??toista", "yhdensiksitoista",
             "yhdensintoista", "yhdensitt??toista", "yhdensinetoista")
        )

        # twelve
        self.assertEqual(
            tuple(n2f(12, to="ordinal", case=c) for c in CASES),
            ("kahdestoista", "kahdennentoista", "kahdettatoista",
             "kahdennessatoista", "kahdennestatoista", "kahdenteentoista",
             "kahdennellatoista", "kahdenneltatoista", "kahdennelletoista",
             "kahdentenatoista", "kahdenneksitoista",
             "kahdensintoista", "kahdennettatoista", "kahdensinetoista")
        )
        self.assertEqual(
            tuple(n2f(12, to="ordinal", case=c, plural=True) for c in CASES),
            ("kahdennettoista", "kahdensientoista", "kahdensiatoista",
             "kahdensissatoista", "kahdensistatoista", "kahdensiintoista",
             "kahdensillatoista", "kahdensiltatoista", "kahdensilletoista",
             "kahdensinatoista", "kahdensiksitoista",
             "kahdensintoista", "kahdensittatoista", "kahdensinetoista")
        )

        # thirteen
        self.assertEqual(
            tuple(n2f(13, to="ordinal", case=c) for c in CASES),
            ("kolmastoista", "kolmannentoista", "kolmattatoista",
             "kolmannessatoista", "kolmannestatoista", "kolmanteentoista",
             "kolmannellatoista", "kolmanneltatoista", "kolmannelletoista",
             "kolmantenatoista", "kolmanneksitoista",
             "kolmansintoista", "kolmannettatoista", "kolmansinetoista")
        )
        self.assertEqual(
            tuple(n2f(13, to="ordinal", case=c, plural=True) for c in CASES),
            ("kolmannettoista", "kolmansientoista", "kolmansiatoista",
             "kolmansissatoista", "kolmansistatoista", "kolmansiintoista",
             "kolmansillatoista", "kolmansiltatoista", "kolmansilletoista",
             "kolmansinatoista", "kolmansiksitoista",
             "kolmansintoista", "kolmansittatoista", "kolmansinetoista")
        )

        # fourteen
        self.assertEqual(
            tuple(n2f(14, to="ordinal", case=c) for c in CASES),
            ("nelj??stoista", "nelj??nnentoista", "nelj??tt??toista",
             "nelj??nness??toista", "nelj??nnest??toista", "nelj??nteentoista",
             "nelj??nnell??toista", "nelj??nnelt??toista", "nelj??nnelletoista",
             "nelj??nten??toista", "nelj??nneksitoista",
             "nelj??nsintoista", "nelj??nnett??toista", "nelj??nsinetoista")
        )
        self.assertEqual(
            tuple(n2f(14, to="ordinal", case=c, plural=True) for c in CASES),
            ("nelj??nnettoista", "nelj??nsientoista", "nelj??nsi??toista",
             "nelj??nsiss??toista", "nelj??nsist??toista", "nelj??nsiintoista",
             "nelj??nsill??toista", "nelj??nsilt??toista", "nelj??nsilletoista",
             "nelj??nsin??toista", "nelj??nsiksitoista",
             "nelj??nsintoista", "nelj??nsitt??toista", "nelj??nsinetoista")
        )

        # fifteen
        self.assertEqual(
            tuple(n2f(15, to="ordinal", case=c) for c in CASES),
            ("viidestoista", "viidennentoista", "viidett??toista",
             "viidenness??toista", "viidennest??toista", "viidenteentoista",
             "viidennell??toista", "viidennelt??toista", "viidennelletoista",
             "viidenten??toista", "viidenneksitoista",
             "viidensintoista", "viidennett??toista", "viidensinetoista")
        )
        self.assertEqual(
            tuple(n2f(15, to="ordinal", case=c, plural=True) for c in CASES),
            ("viidennettoista", "viidensientoista", "viidensi??toista",
             "viidensiss??toista", "viidensist??toista", "viidensiintoista",
             "viidensill??toista", "viidensilt??toista", "viidensilletoista",
             "viidensin??toista", "viidensiksitoista",
             "viidensintoista", "viidensitt??toista", "viidensinetoista")
        )

        # sixteen
        self.assertEqual(
            tuple(n2f(16, to="ordinal", case=c) for c in CASES),
            ("kuudestoista", "kuudennentoista", "kuudettatoista",
             "kuudennessatoista", "kuudennestatoista", "kuudenteentoista",
             "kuudennellatoista", "kuudenneltatoista", "kuudennelletoista",
             "kuudentenatoista", "kuudenneksitoista",
             "kuudensintoista", "kuudennettatoista", "kuudensinetoista")
        )
        self.assertEqual(
            tuple(n2f(16, to="ordinal", case=c, plural=True) for c in CASES),
            ("kuudennettoista", "kuudensientoista", "kuudensiatoista",
             "kuudensissatoista", "kuudensistatoista", "kuudensiintoista",
             "kuudensillatoista", "kuudensiltatoista", "kuudensilletoista",
             "kuudensinatoista", "kuudensiksitoista",
             "kuudensintoista", "kuudensittatoista", "kuudensinetoista")
        )

        # seventeen
        self.assertEqual(
            tuple(n2f(17, to="ordinal", case=c) for c in CASES),
            (
                "seitsem??stoista",
                "seitsem??nnentoista",
                "seitsem??tt??toista",
                "seitsem??nness??toista",
                "seitsem??nnest??toista",
                "seitsem??nteentoista",
                "seitsem??nnell??toista",
                "seitsem??nnelt??toista",
                "seitsem??nnelletoista",
                "seitsem??nten??toista",
                "seitsem??nneksitoista",
                "seitsem??nsintoista",
                "seitsem??nnett??toista",
                "seitsem??nsinetoista"
            )
        )
        self.assertEqual(
            tuple(n2f(17, to="ordinal", case=c, plural=True) for c in CASES),
            (
                "seitsem??nnettoista",
                "seitsem??nsientoista",
                "seitsem??nsi??toista",
                "seitsem??nsiss??toista",
                "seitsem??nsist??toista",
                "seitsem??nsiintoista",
                "seitsem??nsill??toista",
                "seitsem??nsilt??toista",
                "seitsem??nsilletoista",
                "seitsem??nsin??toista",
                "seitsem??nsiksitoista",
                "seitsem??nsintoista",
                "seitsem??nsitt??toista",
                "seitsem??nsinetoista"
            )
        )

        # eighteen
        self.assertEqual(
            tuple(n2f(18, to="ordinal", case=c) for c in CASES),
            (
                "kahdeksastoista",
                "kahdeksannentoista",
                "kahdeksattatoista",
                "kahdeksannessatoista",
                "kahdeksannestatoista",
                "kahdeksanteentoista",
                "kahdeksannellatoista",
                "kahdeksanneltatoista",
                "kahdeksannelletoista",
                "kahdeksantenatoista",
                "kahdeksanneksitoista",
                "kahdeksansintoista",
                "kahdeksannettatoista",
                "kahdeksansinetoista"
            )
        )
        self.assertEqual(
            tuple(n2f(18, to="ordinal", case=c, plural=True) for c in CASES),
            (
                "kahdeksannettoista",
                "kahdeksansientoista",
                "kahdeksansiatoista",
                "kahdeksansissatoista",
                "kahdeksansistatoista",
                "kahdeksansiintoista",
                "kahdeksansillatoista",
                "kahdeksansiltatoista",
                "kahdeksansilletoista",
                "kahdeksansinatoista",
                "kahdeksansiksitoista",
                "kahdeksansintoista",
                "kahdeksansittatoista",
                "kahdeksansinetoista"
            )
        )

        # nineteen
        self.assertEqual(
            tuple(n2f(19, to="ordinal", case=c) for c in CASES),
            (
                "yhdeks??stoista",
                "yhdeks??nnentoista",
                "yhdeks??tt??toista",
                "yhdeks??nness??toista",
                "yhdeks??nnest??toista",
                "yhdeks??nteentoista",
                "yhdeks??nnell??toista",
                "yhdeks??nnelt??toista",
                "yhdeks??nnelletoista",
                "yhdeks??nten??toista",
                "yhdeks??nneksitoista",
                "yhdeks??nsintoista",
                "yhdeks??nnett??toista",
                "yhdeks??nsinetoista"
            )
        )
        self.assertEqual(
            tuple(n2f(19, to="ordinal", case=c, plural=True) for c in CASES),
            (
                "yhdeks??nnettoista",
                "yhdeks??nsientoista",
                "yhdeks??nsi??toista",
                "yhdeks??nsiss??toista",
                "yhdeks??nsist??toista",
                "yhdeks??nsiintoista",
                "yhdeks??nsill??toista",
                "yhdeks??nsilt??toista",
                "yhdeks??nsilletoista",
                "yhdeks??nsin??toista",
                "yhdeks??nsiksitoista",
                "yhdeks??nsintoista",
                "yhdeks??nsitt??toista",
                "yhdeks??nsinetoista"
            )
        )

        # twenty
        self.assertEqual(
            tuple(n2f(20, to="ordinal", case=c) for c in CASES),
            (
                "kahdeskymmenes",
                "kahdennenkymmenennen",
                "kahdettakymmenett??",
                "kahdennessakymmenenness??",
                "kahdennestakymmenennest??",
                "kahdenteenkymmenenteen",
                "kahdennellakymmenennell??",
                "kahdenneltakymmenennelt??",
                "kahdennellekymmenennelle",
                "kahdentenakymmenenten??",
                "kahdenneksikymmenenneksi",
                "kahdensinkymmenensin",
                "kahdennettakymmenennett??",
                "kahdensinekymmenensine"
            )
        )
        self.assertEqual(
            tuple(n2f(20, to="ordinal", case=c, plural=True) for c in CASES),
            (
                "kahdennetkymmenennet",
                "kahdensienkymmenensien",
                "kahdensiakymmenensi??",
                "kahdensissakymmenensiss??",
                "kahdensistakymmenensist??",
                "kahdensiinkymmenensiin",
                "kahdensillakymmenensill??",
                "kahdensiltakymmenensilt??",
                "kahdensillekymmenensille",
                "kahdensinakymmenensin??",
                "kahdensiksikymmenensiksi",
                "kahdensinkymmenensin",
                "kahdensittakymmenensitt??",
                "kahdensinekymmenensine"
            )
        )

    def test_mid(self):

        # thirty
        self.assertEqual(
            tuple(n2f(30, to="cardinal", case=c) for c in CASES),
            ("kolmekymment??", "kolmenkymmenen", "kolmeakymment??",
             "kolmessakymmeness??", "kolmestakymmenest??", "kolmeenkymmeneen",
             "kolmellakymmenell??", "kolmeltakymmenelt??", "kolmellekymmenelle",
             "kolmenakymmenen??", "kolmeksikymmeneksi",
             "kolmenkymmenin", "kolmettakymmenett??", "kolminekymmenine")
        )
        self.assertEqual(
            tuple(n2f(30, to="cardinal", case=c, plural=True) for c in CASES),
            ("kolmetkymmenet", "kolmienkymmenien", "kolmiakymmeni??",
             "kolmissakymmeniss??", "kolmistakymmenist??", "kolmiinkymmeniin",
             "kolmillakymmenill??", "kolmiltakymmenilt??", "kolmillekymmenille",
             "kolminakymmenin??", "kolmiksikymmeniksi",
             "kolminkymmenin", "kolmittakymmenitt??", "kolminekymmenine")
        )

        # forty
        self.assertEqual(
            tuple(n2f(40, to="cardinal", case=c) for c in CASES),
            ("nelj??kymment??", "nelj??nkymmenen", "nelj????kymment??",
             "nelj??ss??kymmeness??", "nelj??st??kymmenest??", "nelj????nkymmeneen",
             "nelj??ll??kymmenell??", "nelj??lt??kymmenelt??", "nelj??llekymmenelle",
             "nelj??n??kymmenen??", "nelj??ksikymmeneksi",
             "neljinkymmenin", "nelj??tt??kymmenett??", "neljinekymmenine")
        )
        self.assertEqual(
            tuple(n2f(40, to="cardinal", case=c, plural=True) for c in CASES),
            ("nelj??tkymmenet", "neljienkymmenien", "nelji??kymmeni??",
             "neljiss??kymmeniss??", "neljist??kymmenist??", "neljiinkymmeniin",
             "neljill??kymmenill??", "neljilt??kymmenilt??", "neljillekymmenille",
             "neljin??kymmenin??", "neljiksikymmeniksi",
             "neljinkymmenin", "neljitt??kymmenitt??", "neljinekymmenine")
        )

        # fifty
        self.assertEqual(
            tuple(n2f(50, to="cardinal", case=c) for c in CASES),
            ("viisikymment??", "viidenkymmenen", "viitt??kymment??",
             "viidess??kymmeness??", "viidest??kymmenest??", "viiteenkymmeneen",
             "viidell??kymmenell??", "viidelt??kymmenelt??", "viidellekymmenelle",
             "viiten??kymmenen??", "viideksikymmeneksi",
             "viisinkymmenin", "viidett??kymmenett??", "viisinekymmenine")
        )
        self.assertEqual(
            tuple(n2f(50, to="cardinal", case=c, plural=True) for c in CASES),
            ("viidetkymmenet", "viisienkymmenien", "viisi??kymmeni??",
             "viisiss??kymmeniss??", "viisist??kymmenist??", "viisiinkymmeniin",
             "viisill??kymmenill??", "viisilt??kymmenilt??", "viisillekymmenille",
             "viisin??kymmenin??", "viisiksikymmeniksi",
             "viisinkymmenin", "viisitt??kymmenitt??", "viisinekymmenine")
        )

        # sixty
        self.assertEqual(
            tuple(n2f(60, to="cardinal", case=c) for c in CASES),
            ("kuusikymment??", "kuudenkymmenen", "kuuttakymment??",
             "kuudessakymmeness??", "kuudestakymmenest??", "kuuteenkymmeneen",
             "kuudellakymmenell??", "kuudeltakymmenelt??", "kuudellekymmenelle",
             "kuutenakymmenen??", "kuudeksikymmeneksi",
             "kuusinkymmenin", "kuudettakymmenett??", "kuusinekymmenine")
        )
        self.assertEqual(
            tuple(n2f(60, to="cardinal", case=c, plural=True) for c in CASES),
            ("kuudetkymmenet", "kuusienkymmenien", "kuusiakymmeni??",
             "kuusissakymmeniss??", "kuusistakymmenist??", "kuusiinkymmeniin",
             "kuusillakymmenill??", "kuusiltakymmenilt??", "kuusillekymmenille",
             "kuusinakymmenin??", "kuusiksikymmeniksi",
             "kuusinkymmenin", "kuusittakymmenitt??", "kuusinekymmenine")
        )

        # seventy
        self.assertEqual(
            tuple(n2f(70, to="cardinal", case=c) for c in CASES),
            (
                "seitsem??nkymment??",
                "seitsem??nkymmenen",
                "seitsem????kymment??",
                "seitsem??ss??kymmeness??",
                "seitsem??st??kymmenest??",
                "seitsem????nkymmeneen",
                "seitsem??ll??kymmenell??",
                "seitsem??lt??kymmenelt??",
                "seitsem??llekymmenelle",
                "seitsem??n??kymmenen??",
                "seitsem??ksikymmeneksi",
                "seitseminkymmenin",
                "seitsem??tt??kymmenett??",
                "seitseminekymmenine"
            )
        )
        self.assertEqual(
            tuple(n2f(70, to="cardinal", case=c, plural=True) for c in CASES),
            (
                "seitsem??tkymmenet",
                "seitsemienkymmenien",
                "seitsemi??kymmeni??",
                "seitsemiss??kymmeniss??",
                "seitsemist??kymmenist??",
                "seitsemiinkymmeniin",
                "seitsemill??kymmenill??",
                "seitsemilt??kymmenilt??",
                "seitsemillekymmenille",
                "seitsemin??kymmenin??",
                "seitsemiksikymmeniksi",
                "seitseminkymmenin",
                "seitsemitt??kymmenitt??",
                "seitseminekymmenine"
            )
        )

        # eighty
        self.assertEqual(
            tuple(n2f(80, to="cardinal", case=c) for c in CASES),
            (
                "kahdeksankymment??",
                "kahdeksankymmenen",
                "kahdeksaakymment??",
                "kahdeksassakymmeness??",
                "kahdeksastakymmenest??",
                "kahdeksaankymmeneen",
                "kahdeksallakymmenell??",
                "kahdeksaltakymmenelt??",
                "kahdeksallekymmenelle",
                "kahdeksanakymmenen??",
                "kahdeksaksikymmeneksi",
                "kahdeksinkymmenin",
                "kahdeksattakymmenett??",
                "kahdeksinekymmenine"
            )
        )
        self.assertEqual(
            tuple(n2f(80, to="cardinal", case=c, plural=True) for c in CASES),
            (
                "kahdeksatkymmenet",
                "kahdeksienkymmenien",
                "kahdeksiakymmeni??",
                "kahdeksissakymmeniss??",
                "kahdeksistakymmenist??",
                "kahdeksiinkymmeniin",
                "kahdeksillakymmenill??",
                "kahdeksiltakymmenilt??",
                "kahdeksillekymmenille",
                "kahdeksinakymmenin??",
                "kahdeksiksikymmeniksi",
                "kahdeksinkymmenin",
                "kahdeksittakymmenitt??",
                "kahdeksinekymmenine"
            )
        )

        # ninety
        self.assertEqual(
            tuple(n2f(90, to="cardinal", case=c) for c in CASES),
            (
                "yhdeks??nkymment??",
                "yhdeks??nkymmenen",
                "yhdeks????kymment??",
                "yhdeks??ss??kymmeness??",
                "yhdeks??st??kymmenest??",
                "yhdeks????nkymmeneen",
                "yhdeks??ll??kymmenell??",
                "yhdeks??lt??kymmenelt??",
                "yhdeks??llekymmenelle",
                "yhdeks??n??kymmenen??",
                "yhdeks??ksikymmeneksi",
                "yhdeksinkymmenin",
                "yhdeks??tt??kymmenett??",
                "yhdeksinekymmenine"
            )
        )
        self.assertEqual(
            tuple(n2f(90, to="cardinal", case=c, plural=True) for c in CASES),
            (
                "yhdeks??tkymmenet",
                "yhdeksienkymmenien",
                "yhdeksi??kymmeni??",
                "yhdeksiss??kymmeniss??",
                "yhdeksist??kymmenist??",
                "yhdeksiinkymmeniin",
                "yhdeksill??kymmenill??",
                "yhdeksilt??kymmenilt??",
                "yhdeksillekymmenille",
                "yhdeksin??kymmenin??",
                "yhdeksiksikymmeniksi",
                "yhdeksinkymmenin",
                "yhdeksitt??kymmenitt??",
                "yhdeksinekymmenine"
            )
        )

        # one hundred
        self.assertEqual(
            tuple(n2f(100, to="cardinal", case=c) for c in CASES),
            ("sata", "sadan", "sataa",
             "sadassa", "sadasta", "sataan",
             "sadalla", "sadalta", "sadalle",
             "satana", "sadaksi",
             "sadoin", "sadatta", "satoine")
        )
        self.assertEqual(
            tuple(n2f(100, to="cardinal", case=c, plural=True) for c in CASES),
            ("sadat", "satojen", "satoja",
             "sadoissa", "sadoista", "satoihin",
             "sadoilla", "sadoilta", "sadoille",
             "satoina", "sadoiksi",
             "sadoin", "sadoitta", "satoine")
        )

        # one hundred and twenty-three
        self.assertEqual(
            tuple(n2f(123, to="cardinal", case=c) for c in CASES),
            (
                "satakaksikymment??kolme",
                "sadankahdenkymmenenkolmen",
                "sataakahtakymment??kolmea",
                "sadassakahdessakymmeness??kolmessa",
                "sadastakahdestakymmenest??kolmesta",
                "sataankahteenkymmeneenkolmeen",
                "sadallakahdellakymmenell??kolmella",
                "sadaltakahdeltakymmenelt??kolmelta",
                "sadallekahdellekymmenellekolmelle",
                "satanakahtenakymmenen??kolmena",
                "sadaksikahdeksikymmeneksikolmeksi",
                "sadoinkaksinkymmeninkolmen",
                "sadattakahdettakymmenett??kolmetta",
                "satoinekaksinekymmeninekolmine"
            )
        )
        self.assertEqual(
            tuple(n2f(123, to="cardinal", case=c, plural=True) for c in CASES),
            (
                "sadatkahdetkymmenetkolmet",
                "satojenkaksienkymmenienkolmien",
                "satojakaksiakymmeni??kolmia",
                "sadoissakaksissakymmeniss??kolmissa",
                "sadoistakaksistakymmenist??kolmista",
                "satoihinkaksiinkymmeniinkolmiin",
                "sadoillakaksillakymmenill??kolmilla",
                "sadoiltakaksiltakymmenilt??kolmilta",
                "sadoillekaksillekymmenillekolmille",
                "satoinakaksinakymmenin??kolmina",
                "sadoiksikaksiksikymmeniksikolmiksi",
                "sadoinkaksinkymmeninkolmin",
                "sadoittakaksittakymmenitt??kolmitta",
                "satoinekaksinekymmeninekolmine"
            )
        )

        # one thousand
        self.assertEqual(
            tuple(n2f(1000, to="cardinal", case=c) for c in CASES),
            ("tuhat", "tuhannen", "tuhatta",
             "tuhannessa", "tuhannesta", "tuhanteen",
             "tuhannella", "tuhannelta", "tuhannelle",
             "tuhantena", "tuhanneksi",
             "tuhansin", "tuhannetta", "tuhansine")
        )
        self.assertEqual(
            tuple(n2f(1000, to="cardinal", case=c, plural=True)
                  for c in CASES),
            ("tuhannet", "tuhansien", "tuhansia",
             "tuhansissa", "tuhansista", "tuhansiin",
             "tuhansilla", "tuhansilta", "tuhansille",
             "tuhansina", "tuhansiksi",
             "tuhansin", "tuhansitta", "tuhansine")
        )

        # one thousand, two hundred and thirty-four
        self.assertEqual(
            tuple(n2f(1234, to="cardinal", case=c) for c in CASES),
            (
                "tuhat kaksisataakolmekymment??nelj??",
                "tuhannen kahdensadankolmenkymmenennelj??n",
                "tuhatta kahtasataakolmeakymment??nelj????",
                "tuhannessa kahdessasadassakolmessakymmeness??nelj??ss??",
                "tuhannesta kahdestasadastakolmestakymmenest??nelj??st??",
                "tuhanteen kahteensataankolmeenkymmeneennelj????n",
                "tuhannella kahdellasadallakolmellakymmenell??nelj??ll??",
                "tuhannelta kahdeltasadaltakolmeltakymmenelt??nelj??lt??",
                "tuhannelle kahdellesadallekolmellekymmenellenelj??lle",
                "tuhantena kahtenasatanakolmenakymmenen??nelj??n??",
                "tuhanneksi kahdeksisadaksikolmeksikymmeneksinelj??ksi",
                "tuhansin kaksinsadoinkolmenkymmeninneljin",
                "tuhannetta kahdettasadattakolmettakymmenett??nelj??tt??",
                "tuhansine kaksinesatoinekolminekymmenineneljine"
            )
        )
        self.assertEqual(
            tuple(n2f(1234, to="cardinal", case=c, plural=True)
                  for c in CASES),
            (
                "tuhannet kahdetsadatkolmetkymmenetnelj??t",
                "tuhansien kaksiensatojenkolmienkymmenienneljien",
                "tuhansia kaksiasatojakolmiakymmeni??nelji??",
                "tuhansissa kaksissasadoissakolmissakymmeniss??neljiss??",
                "tuhansista kaksistasadoistakolmistakymmenist??neljist??",
                "tuhansiin kaksiinsatoihinkolmiinkymmeniinneljiin",
                "tuhansilla kaksillasadoillakolmillakymmenill??neljill??",
                "tuhansilta kaksiltasadoiltakolmiltakymmenilt??neljilt??",
                "tuhansille kaksillesadoillekolmillekymmenilleneljille",
                "tuhansina kaksinasatoinakolminakymmenin??neljin??",
                "tuhansiksi kaksiksisadoiksikolmiksikymmeniksineljiksi",
                "tuhansin kaksinsadoinkolminkymmeninneljin",
                "tuhansitta kaksittasadoittakolmittakymmenitt??neljitt??",
                "tuhansine kaksinesatoinekolminekymmenineneljine"
            )
        )

    def test_mid_ord(self):

        # thirty
        self.assertEqual(
            tuple(n2f(30, to="ordinal", case=c) for c in CASES),
            (
                "kolmaskymmenes",
                "kolmannenkymmenennen",
                "kolmattakymmenett??",
                "kolmannessakymmenenness??",
                "kolmannestakymmenennest??",
                "kolmanteenkymmenenteen",
                "kolmannellakymmenennell??",
                "kolmanneltakymmenennelt??",
                "kolmannellekymmenennelle",
                "kolmantenakymmenenten??",
                "kolmanneksikymmenenneksi",
                "kolmansinkymmenensin",
                "kolmannettakymmenennett??",
                "kolmansinekymmenensine"
            )
        )
        self.assertEqual(
            tuple(n2f(30, to="ordinal", case=c, plural=True) for c in CASES),
            (
                "kolmannetkymmenennet",
                "kolmansienkymmenensien",
                "kolmansiakymmenensi??",
                "kolmansissakymmenensiss??",
                "kolmansistakymmenensist??",
                "kolmansiinkymmenensiin",
                "kolmansillakymmenensill??",
                "kolmansiltakymmenensilt??",
                "kolmansillekymmenensille",
                "kolmansinakymmenensin??",
                "kolmansiksikymmenensiksi",
                "kolmansinkymmenensin",
                "kolmansittakymmenensitt??",
                "kolmansinekymmenensine"
            )
        )

        # forty
        self.assertEqual(
            tuple(n2f(40, to="ordinal", case=c) for c in CASES),
            (
                "nelj??skymmenes",
                "nelj??nnenkymmenennen",
                "nelj??tt??kymmenett??",
                "nelj??nness??kymmenenness??",
                "nelj??nnest??kymmenennest??",
                "nelj??nteenkymmenenteen",
                "nelj??nnell??kymmenennell??",
                "nelj??nnelt??kymmenennelt??",
                "nelj??nnellekymmenennelle",
                "nelj??nten??kymmenenten??",
                "nelj??nneksikymmenenneksi",
                "nelj??nsinkymmenensin",
                "nelj??nnett??kymmenennett??",
                "nelj??nsinekymmenensine"
            )
        )
        self.assertEqual(
            tuple(n2f(40, to="ordinal", case=c, plural=True) for c in CASES),
            (
                "nelj??nnetkymmenennet",
                "nelj??nsienkymmenensien",
                "nelj??nsi??kymmenensi??",
                "nelj??nsiss??kymmenensiss??",
                "nelj??nsist??kymmenensist??",
                "nelj??nsiinkymmenensiin",
                "nelj??nsill??kymmenensill??",
                "nelj??nsilt??kymmenensilt??",
                "nelj??nsillekymmenensille",
                "nelj??nsin??kymmenensin??",
                "nelj??nsiksikymmenensiksi",
                "nelj??nsinkymmenensin",
                "nelj??nsitt??kymmenensitt??",
                "nelj??nsinekymmenensine"
            )
        )

        # fifty
        self.assertEqual(
            tuple(n2f(50, to="ordinal", case=c) for c in CASES),
            (
                "viideskymmenes",
                "viidennenkymmenennen",
                "viidett??kymmenett??",
                "viidenness??kymmenenness??",
                "viidennest??kymmenennest??",
                "viidenteenkymmenenteen",
                "viidennell??kymmenennell??",
                "viidennelt??kymmenennelt??",
                "viidennellekymmenennelle",
                "viidenten??kymmenenten??",
                "viidenneksikymmenenneksi",
                "viidensinkymmenensin",
                "viidennett??kymmenennett??",
                "viidensinekymmenensine"
            )
        )
        self.assertEqual(
            tuple(n2f(50, to="ordinal", case=c, plural=True) for c in CASES),
            (
                "viidennetkymmenennet",
                "viidensienkymmenensien",
                "viidensi??kymmenensi??",
                "viidensiss??kymmenensiss??",
                "viidensist??kymmenensist??",
                "viidensiinkymmenensiin",
                "viidensill??kymmenensill??",
                "viidensilt??kymmenensilt??",
                "viidensillekymmenensille",
                "viidensin??kymmenensin??",
                "viidensiksikymmenensiksi",
                "viidensinkymmenensin",
                "viidensitt??kymmenensitt??",
                "viidensinekymmenensine"
            )
        )

        # sixty
        self.assertEqual(
            tuple(n2f(60, to="ordinal", case=c) for c in CASES),
            (
                "kuudeskymmenes",
                "kuudennenkymmenennen",
                "kuudettakymmenett??",
                "kuudennessakymmenenness??",
                "kuudennestakymmenennest??",
                "kuudenteenkymmenenteen",
                "kuudennellakymmenennell??",
                "kuudenneltakymmenennelt??",
                "kuudennellekymmenennelle",
                "kuudentenakymmenenten??",
                "kuudenneksikymmenenneksi",
                "kuudensinkymmenensin",
                "kuudennettakymmenennett??",
                "kuudensinekymmenensine"
            )
        )
        self.assertEqual(
            tuple(n2f(60, to="ordinal", case=c, plural=True) for c in CASES),
            (
                "kuudennetkymmenennet",
                "kuudensienkymmenensien",
                "kuudensiakymmenensi??",
                "kuudensissakymmenensiss??",
                "kuudensistakymmenensist??",
                "kuudensiinkymmenensiin",
                "kuudensillakymmenensill??",
                "kuudensiltakymmenensilt??",
                "kuudensillekymmenensille",
                "kuudensinakymmenensin??",
                "kuudensiksikymmenensiksi",
                "kuudensinkymmenensin",
                "kuudensittakymmenensitt??",
                "kuudensinekymmenensine"
            )
        )

        # seventy
        self.assertEqual(
            tuple(n2f(70, to="ordinal", case=c) for c in CASES),
            (
                "seitsem??skymmenes",
                "seitsem??nnenkymmenennen",
                "seitsem??tt??kymmenett??",
                "seitsem??nness??kymmenenness??",
                "seitsem??nnest??kymmenennest??",
                "seitsem??nteenkymmenenteen",
                "seitsem??nnell??kymmenennell??",
                "seitsem??nnelt??kymmenennelt??",
                "seitsem??nnellekymmenennelle",
                "seitsem??nten??kymmenenten??",
                "seitsem??nneksikymmenenneksi",
                "seitsem??nsinkymmenensin",
                "seitsem??nnett??kymmenennett??",
                "seitsem??nsinekymmenensine"
            )
        )
        self.assertEqual(
            tuple(n2f(70, to="ordinal", case=c, plural=True) for c in CASES),
            (
                "seitsem??nnetkymmenennet",
                "seitsem??nsienkymmenensien",
                "seitsem??nsi??kymmenensi??",
                "seitsem??nsiss??kymmenensiss??",
                "seitsem??nsist??kymmenensist??",
                "seitsem??nsiinkymmenensiin",
                "seitsem??nsill??kymmenensill??",
                "seitsem??nsilt??kymmenensilt??",
                "seitsem??nsillekymmenensille",
                "seitsem??nsin??kymmenensin??",
                "seitsem??nsiksikymmenensiksi",
                "seitsem??nsinkymmenensin",
                "seitsem??nsitt??kymmenensitt??",
                "seitsem??nsinekymmenensine"
            )
        )

        # eighty
        self.assertEqual(
            tuple(n2f(80, to="ordinal", case=c) for c in CASES),
            (
                "kahdeksaskymmenes",
                "kahdeksannenkymmenennen",
                "kahdeksattakymmenett??",
                "kahdeksannessakymmenenness??",
                "kahdeksannestakymmenennest??",
                "kahdeksanteenkymmenenteen",
                "kahdeksannellakymmenennell??",
                "kahdeksanneltakymmenennelt??",
                "kahdeksannellekymmenennelle",
                "kahdeksantenakymmenenten??",
                "kahdeksanneksikymmenenneksi",
                "kahdeksansinkymmenensin",
                "kahdeksannettakymmenennett??",
                "kahdeksansinekymmenensine"
            )
        )
        self.assertEqual(
            tuple(n2f(80, to="ordinal", case=c, plural=True) for c in CASES),
            (
                "kahdeksannetkymmenennet",
                "kahdeksansienkymmenensien",
                "kahdeksansiakymmenensi??",
                "kahdeksansissakymmenensiss??",
                "kahdeksansistakymmenensist??",
                "kahdeksansiinkymmenensiin",
                "kahdeksansillakymmenensill??",
                "kahdeksansiltakymmenensilt??",
                "kahdeksansillekymmenensille",
                "kahdeksansinakymmenensin??",
                "kahdeksansiksikymmenensiksi",
                "kahdeksansinkymmenensin",
                "kahdeksansittakymmenensitt??",
                "kahdeksansinekymmenensine"
            )
        )

        # ninety
        self.assertEqual(
            tuple(n2f(90, to="ordinal", case=c) for c in CASES),
            (
                "yhdeks??skymmenes",
                "yhdeks??nnenkymmenennen",
                "yhdeks??tt??kymmenett??",
                "yhdeks??nness??kymmenenness??",
                "yhdeks??nnest??kymmenennest??",
                "yhdeks??nteenkymmenenteen",
                "yhdeks??nnell??kymmenennell??",
                "yhdeks??nnelt??kymmenennelt??",
                "yhdeks??nnellekymmenennelle",
                "yhdeks??nten??kymmenenten??",
                "yhdeks??nneksikymmenenneksi",
                "yhdeks??nsinkymmenensin",
                "yhdeks??nnett??kymmenennett??",
                "yhdeks??nsinekymmenensine"
            )
        )
        self.assertEqual(
            tuple(n2f(90, to="ordinal", case=c, plural=True) for c in CASES),
            (
                "yhdeks??nnetkymmenennet",
                "yhdeks??nsienkymmenensien",
                "yhdeks??nsi??kymmenensi??",
                "yhdeks??nsiss??kymmenensiss??",
                "yhdeks??nsist??kymmenensist??",
                "yhdeks??nsiinkymmenensiin",
                "yhdeks??nsill??kymmenensill??",
                "yhdeks??nsilt??kymmenensilt??",
                "yhdeks??nsillekymmenensille",
                "yhdeks??nsin??kymmenensin??",
                "yhdeks??nsiksikymmenensiksi",
                "yhdeks??nsinkymmenensin",
                "yhdeks??nsitt??kymmenensitt??",
                "yhdeks??nsinekymmenensine"
            )
        )

        # one hundred
        self.assertEqual(
            tuple(n2f(100, to="ordinal", case=c) for c in CASES),
            ("sadas", "sadannen", "sadatta",
             "sadannessa", "sadannesta", "sadanteen",
             "sadannella", "sadannelta", "sadannelle",
             "sadantena", "sadanneksi",
             "sadansin", "sadannetta", "sadansine")
        )
        self.assertEqual(
            tuple(n2f(100, to="ordinal", case=c, plural=True) for c in CASES),
            ("sadannet", "sadansien", "sadansia",
             "sadansissa", "sadansista", "sadansiin",
             "sadansilla", "sadansilta", "sadansille",
             "sadansina", "sadansiksi",
             "sadansin", "sadansitta", "sadansine")
        )

        # one hundred and twenty-three
        self.assertEqual(
            tuple(n2f(123, to="ordinal", case=c) for c in CASES),
            (
                "sadaskahdeskymmeneskolmas",
                "sadannenkahdennenkymmenennenkolmannen",
                "sadattakahdettakymmenett??kolmatta",
                "sadannessakahdennessakymmenenness??kolmannessa",
                "sadannestakahdennestakymmenennest??kolmannesta",
                "sadanteenkahdenteenkymmenenteenkolmanteen",
                "sadannellakahdennellakymmenennell??kolmannella",
                "sadanneltakahdenneltakymmenennelt??kolmannelta",
                "sadannellekahdennellekymmenennellekolmannelle",
                "sadantenakahdentenakymmenenten??kolmantena",
                "sadanneksikahdenneksikymmenenneksikolmanneksi",
                "sadansinkahdensinkymmenensinkolmansin",
                "sadannettakahdennettakymmenennett??kolmannetta",
                "sadansinekahdensinekymmenensinekolmansine"
            )
        )
        self.assertEqual(
            tuple(n2f(123, to="ordinal", case=c, plural=True) for c in CASES),
            (
                "sadannetkahdennetkymmenennetkolmannet",
                "sadansienkahdensienkymmenensienkolmansien",
                "sadansiakahdensiakymmenensi??kolmansia",
                "sadansissakahdensissakymmenensiss??kolmansissa",
                "sadansistakahdensistakymmenensist??kolmansista",
                "sadansiinkahdensiinkymmenensiinkolmansiin",
                "sadansillakahdensillakymmenensill??kolmansilla",
                "sadansiltakahdensiltakymmenensilt??kolmansilta",
                "sadansillekahdensillekymmenensillekolmansille",
                "sadansinakahdensinakymmenensin??kolmansina",
                "sadansiksikahdensiksikymmenensiksikolmansiksi",
                "sadansinkahdensinkymmenensinkolmansin",
                "sadansittakahdensittakymmenensitt??kolmansitta",
                "sadansinekahdensinekymmenensinekolmansine"
            )
        )

        # one thousand
        self.assertEqual(
            tuple(n2f(1000, to="ordinal", case=c) for c in CASES),
            ("tuhannes", "tuhannennen", "tuhannetta",
             "tuhannennessa", "tuhannennesta", "tuhannenteen",
             "tuhannennella", "tuhannennelta", "tuhannennelle",
             "tuhannentena", "tuhannenneksi",
             "tuhannensin", "tuhannennetta", "tuhannensine")
        )
        self.assertEqual(
            tuple(n2f(1000, to="ordinal", case=c, plural=True) for c in CASES),
            ("tuhannennet", "tuhannensien", "tuhannensia",
             "tuhannensissa", "tuhannensista", "tuhannensiin",
             "tuhannensilla", "tuhannensilta", "tuhannensille",
             "tuhannensina", "tuhannensiksi",
             "tuhannensin", "tuhannensitta", "tuhannensine")
        )

        # one thousand, two hundred and thirty-four
        self.assertEqual(
            tuple(n2f(1234, to="ordinal", case=c) for c in CASES),
            (
                "tuhannes kahdessadaskolmaskymmenesnelj??s",
                "tuhannennen kahdennensadannenkolmannenkymmenennennelj??nnen",
                "tuhannetta kahdettasadattakolmattakymmenett??nelj??tt??",
                "tuhannennessa kahdennessasadannessa"
                "kolmannessakymmenenness??nelj??nness??",
                "tuhannennesta kahdennestasadannesta"
                "kolmannestakymmenennest??nelj??nnest??",
                "tuhannenteen kahdenteensadanteen"
                "kolmanteenkymmenenteennelj??nteen",
                "tuhannennella kahdennellasadannella"
                "kolmannellakymmenennell??nelj??nnell??",
                "tuhannennelta kahdenneltasadannelta"
                "kolmanneltakymmenennelt??nelj??nnelt??",
                "tuhannennelle kahdennellesadannelle"
                "kolmannellekymmenennellenelj??nnelle",
                "tuhannentena kahdentenasadantena"
                "kolmantenakymmenenten??nelj??nten??",
                "tuhannenneksi kahdenneksisadanneksi"
                "kolmanneksikymmenenneksinelj??nneksi",
                "tuhannensin kahdensinsadansin"
                "kolmansinkymmenensinnelj??nsin",
                "tuhannennetta kahdennettasadannetta"
                "kolmannettakymmenennett??nelj??nnett??",
                "tuhannensine kahdensinesadansine"
                "kolmansinekymmenensinenelj??nsine"
            )
        )
        self.assertEqual(
            tuple(n2f(1234, to="ordinal", case=c, plural=True) for c in CASES),
            (
                "tuhannennet kahdennetsadannet"
                "kolmannetkymmenennetnelj??nnet",
                "tuhannensien kahdensiensadansien"
                "kolmansienkymmenensiennelj??nsien",
                "tuhannensia kahdensiasadansia"
                "kolmansiakymmenensi??nelj??nsi??",
                "tuhannensissa kahdensissasadansissa"
                "kolmansissakymmenensiss??nelj??nsiss??",
                "tuhannensista kahdensistasadansista"
                "kolmansistakymmenensist??nelj??nsist??",
                "tuhannensiin kahdensiinsadansiin"
                "kolmansiinkymmenensiinnelj??nsiin",
                "tuhannensilla kahdensillasadansilla"
                "kolmansillakymmenensill??nelj??nsill??",
                "tuhannensilta kahdensiltasadansilta"
                "kolmansiltakymmenensilt??nelj??nsilt??",
                "tuhannensille kahdensillesadansille"
                "kolmansillekymmenensillenelj??nsille",
                "tuhannensina kahdensinasadansina"
                "kolmansinakymmenensin??nelj??nsin??",
                "tuhannensiksi kahdensiksisadansiksi"
                "kolmansiksikymmenensiksinelj??nsiksi",
                "tuhannensin kahdensinsadansin"
                "kolmansinkymmenensinnelj??nsin",
                "tuhannensitta kahdensittasadansitta"
                "kolmansittakymmenensitt??nelj??nsitt??",
                "tuhannensine kahdensinesadansine"
                "kolmansinekymmenensinenelj??nsine"
            )
        )

    def test_high(self):

        # ten thousand
        self.assertEqual(
            tuple(n2f(10000, to="cardinal", case=c) for c in CASES),
            (
                "kymmenentuhatta",
                "kymmenentuhannen",
                "kymment??tuhatta",
                "kymmeness??tuhannessa",
                "kymmenest??tuhannesta",
                "kymmeneentuhanteen",
                "kymmenell??tuhannella",
                "kymmenelt??tuhannelta",
                "kymmenelletuhannelle",
                "kymmenen??tuhantena",
                "kymmeneksituhanneksi",
                "kymmenintuhansin",
                "kymmenett??tuhannetta",
                "kymmeninetuhansine"
            )
        )
        self.assertEqual(
            tuple(n2f(10000, to="cardinal", case=c, plural=True)
                  for c in CASES),
            (
                "kymmenettuhannet",
                "kymmenientuhansien",
                "kymmeni??tuhansia",
                "kymmeniss??tuhansissa",
                "kymmenist??tuhansista",
                "kymmeniintuhansiin",
                "kymmenill??tuhansilla",
                "kymmenilt??tuhansilta",
                "kymmenilletuhansille",
                "kymmenin??tuhansina",
                "kymmeniksituhansiksi",
                "kymmenintuhansin",
                "kymmenitt??tuhansitta",
                "kymmeninetuhansine"
            )
        )

        # twelve thousand, three hundred and forty-five
        self.assertEqual(
            tuple(n2f(12345, to="cardinal", case=c) for c in CASES),
            (
                "kaksitoistatuhatta "
                "kolmesataanelj??kymment??viisi",
                "kahdentoistatuhannen "
                "kolmensadannelj??nkymmenenviiden",
                "kahtatoistatuhatta "
                "kolmeasataanelj????kymment??viitt??",
                "kahdessatoistatuhannessa "
                "kolmessasadassanelj??ss??kymmeness??viidess??",
                "kahdestatoistatuhannesta "
                "kolmestasadastanelj??st??kymmenest??viidest??",
                "kahteentoistatuhanteen "
                "kolmeensataannelj????nkymmeneenviiteen",
                "kahdellatoistatuhannella "
                "kolmellasadallanelj??ll??kymmenell??viidell??",
                "kahdeltatoistatuhannelta "
                "kolmeltasadaltanelj??lt??kymmenelt??viidelt??",
                "kahdelletoistatuhannelle "
                "kolmellesadallenelj??llekymmenelleviidelle",
                "kahtenatoistatuhantena "
                "kolmenasatananelj??n??kymmenen??viiten??",
                "kahdeksitoistatuhanneksi "
                "kolmeksisadaksinelj??ksikymmeneksiviideksi",
                "kaksintoistatuhansin "
                "kolmensadoinneljinkymmeninviisin",
                "kahdettatoistatuhannetta "
                "kolmettasadattanelj??tt??kymmenett??viidett??",
                "kaksinetoistatuhansine "
                "kolminesatoineneljinekymmenineviisine"
            )
        )
        self.assertEqual(
            tuple(n2f(
                12345, to="cardinal", case=c, plural=True) for c in CASES),
            (
                "kahdettoistatuhannet "
                "kolmetsadatnelj??tkymmenetviidet",
                "kaksientoistatuhansien "
                "kolmiensatojenneljienkymmenienviisien",
                "kaksiatoistatuhansia "
                "kolmiasatojanelji??kymmeni??viisi??",
                "kaksissatoistatuhansissa "
                "kolmissasadoissaneljiss??kymmeniss??viisiss??",
                "kaksistatoistatuhansista "
                "kolmistasadoistaneljist??kymmenist??viisist??",
                "kaksiintoistatuhansiin "
                "kolmiinsatoihinneljiinkymmeniinviisiin",
                "kaksillatoistatuhansilla "
                "kolmillasadoillaneljill??kymmenill??viisill??",
                "kaksiltatoistatuhansilta "
                "kolmiltasadoiltaneljilt??kymmenilt??viisilt??",
                "kaksilletoistatuhansille "
                "kolmillesadoilleneljillekymmenilleviisille",
                "kaksinatoistatuhansina "
                "kolminasatoinaneljin??kymmenin??viisin??",
                "kaksiksitoistatuhansiksi "
                "kolmiksisadoiksineljiksikymmeniksiviisiksi",
                "kaksintoistatuhansin "
                "kolminsadoinneljinkymmeninviisin",
                "kaksittatoistatuhansitta "
                "kolmittasadoittaneljitt??kymmenitt??viisitt??",
                "kaksinetoistatuhansine "
                "kolminesatoineneljinekymmenineviisine"
            )
        )

        # one hundred thousand
        self.assertEqual(
            tuple(n2f(100000, to="cardinal", case=c) for c in CASES),
            ("satatuhatta", "sadantuhannen", "sataatuhatta",
             "sadassatuhannessa", "sadastatuhannesta", "sataantuhanteen",
             "sadallatuhannella", "sadaltatuhannelta", "sadalletuhannelle",
             "satanatuhantena", "sadaksituhanneksi",
             "sadointuhansin", "sadattatuhannetta", "satoinetuhansine")
        )
        self.assertEqual(
            tuple(n2f(100000, to="cardinal", case=c, plural=True)
                  for c in CASES),
            ("sadattuhannet", "satojentuhansien", "satojatuhansia",
             "sadoissatuhansissa", "sadoistatuhansista", "satoihintuhansiin",
             "sadoillatuhansilla", "sadoiltatuhansilta", "sadoilletuhansille",
             "satoinatuhansina", "sadoiksituhansiksi",
             "sadointuhansin", "sadoittatuhansitta", "satoinetuhansine")
        )

        # one hundred and twenty-three thousand, four hundred and fifty-six
        self.assertEqual(
            tuple(n2f(123456, to="cardinal", case=c) for c in CASES),
            (
                "satakaksikymment??kolmetuhatta "
                "nelj??sataaviisikymment??kuusi",
                "sadankahdenkymmenenkolmentuhannen "
                "nelj??nsadanviidenkymmenenkuuden",
                "sataakahtakymment??kolmeatuhatta "
                "nelj????sataaviitt??kymment??kuutta",
                "sadassakahdessakymmeness??kolmessatuhannessa "
                "nelj??ss??sadassaviidess??kymmeness??kuudessa",
                "sadastakahdestakymmenest??kolmestatuhannesta "
                "nelj??st??sadastaviidest??kymmenest??kuudesta",
                "sataankahteenkymmeneenkolmeentuhanteen "
                "nelj????nsataanviiteenkymmeneenkuuteen",
                "sadallakahdellakymmenell??kolmellatuhannella "
                "nelj??ll??sadallaviidell??kymmenell??kuudella",
                "sadaltakahdeltakymmenelt??kolmeltatuhannelta "
                "nelj??lt??sadaltaviidelt??kymmenelt??kuudelta",
                "sadallekahdellekymmenellekolmelletuhannelle "
                "nelj??llesadalleviidellekymmenellekuudelle",
                "satanakahtenakymmenen??kolmenatuhantena "
                "nelj??n??satanaviiten??kymmenen??kuutena",
                "sadaksikahdeksikymmeneksikolmeksituhanneksi "
                "nelj??ksisadaksiviideksikymmeneksikuudeksi",
                "sadoinkaksinkymmeninkolmentuhansin "
                "neljinsadoinviisinkymmeninkuusin",
                "sadattakahdettakymmenett??kolmettatuhannetta "
                "nelj??tt??sadattaviidett??kymmenett??kuudetta",
                "satoinekaksinekymmeninekolminetuhansine "
                "neljinesatoineviisinekymmeninekuusine"
            )
        )
        self.assertEqual(
            tuple(n2f(123456, to="cardinal", case=c, plural=True)
                  for c in CASES),
            (
                "sadatkahdetkymmenetkolmettuhannet "
                "nelj??tsadatviidetkymmenetkuudet",
                "satojenkaksienkymmenienkolmientuhansien "
                "neljiensatojenviisienkymmenienkuusien",
                "satojakaksiakymmeni??kolmiatuhansia "
                "nelji??satojaviisi??kymmeni??kuusia",
                "sadoissakaksissakymmeniss??kolmissatuhansissa "
                "neljiss??sadoissaviisiss??kymmeniss??kuusissa",
                "sadoistakaksistakymmenist??kolmistatuhansista "
                "neljist??sadoistaviisist??kymmenist??kuusista",
                "satoihinkaksiinkymmeniinkolmiintuhansiin "
                "neljiinsatoihinviisiinkymmeniinkuusiin",
                "sadoillakaksillakymmenill??kolmillatuhansilla "
                "neljill??sadoillaviisill??kymmenill??kuusilla",
                "sadoiltakaksiltakymmenilt??kolmiltatuhansilta "
                "neljilt??sadoiltaviisilt??kymmenilt??kuusilta",
                "sadoillekaksillekymmenillekolmilletuhansille "
                "neljillesadoilleviisillekymmenillekuusille",
                "satoinakaksinakymmenin??kolminatuhansina "
                "neljin??satoinaviisin??kymmenin??kuusina",
                "sadoiksikaksiksikymmeniksikolmiksituhansiksi "
                "neljiksisadoiksiviisiksikymmeniksikuusiksi",
                "sadoinkaksinkymmeninkolmintuhansin "
                "neljinsadoinviisinkymmeninkuusin",
                "sadoittakaksittakymmenitt??kolmittatuhansitta "
                "neljitt??sadoittaviisitt??kymmenitt??kuusitta",
                "satoinekaksinekymmeninekolminetuhansine "
                "neljinesatoineviisinekymmeninekuusine"
            )
        )

        # one million
        self.assertEqual(
            tuple(n2f(10**6, to="cardinal", case=c) for c in CASES),
            ("miljoona", "miljoonan", "miljoonaa",
             "miljoonassa", "miljoonasta", "miljoonaan",
             "miljoonalla", "miljoonalta", "miljoonalle",
             "miljoonana", "miljoonaksi",
             "miljoonin", "miljoonatta", "miljoonine")
        )
        self.assertEqual(
            tuple(n2f(10**6, to="cardinal", case=c, plural=True)
                  for c in CASES),
            ("miljoonat", "miljoonien", "miljoonia",
             "miljoonissa", "miljoonista", "miljooniin",
             "miljoonilla", "miljoonilta", "miljoonille",
             "miljoonina", "miljooniksi",
             "miljoonin", "miljoonitta", "miljoonine")
        )

        # one million, two hundred and thirty-four thousand,
        # five hundred and sixty-seven
        self.assertEqual(
            tuple(n2f(1234567, to="cardinal", case=c) for c in CASES),
            (
                "miljoona "
                "kaksisataakolmekymment??nelj??tuhatta "
                "viisisataakuusikymment??seitsem??n",
                "miljoonan "
                "kahdensadankolmenkymmenennelj??ntuhannen "
                "viidensadankuudenkymmenenseitsem??n",
                "miljoonaa "
                "kahtasataakolmeakymment??nelj????tuhatta "
                "viitt??sataakuuttakymment??seitsem????",
                "miljoonassa "
                "kahdessasadassakolmessakymmeness??nelj??ss??tuhannessa "
                "viidess??sadassakuudessakymmeness??seitsem??ss??",
                "miljoonasta "
                "kahdestasadastakolmestakymmenest??nelj??st??tuhannesta "
                "viidest??sadastakuudestakymmenest??seitsem??st??",
                "miljoonaan "
                "kahteensataankolmeenkymmeneennelj????ntuhanteen "
                "viiteensataankuuteenkymmeneenseitsem????n",
                "miljoonalla "
                "kahdellasadallakolmellakymmenell??nelj??ll??tuhannella "
                "viidell??sadallakuudellakymmenell??seitsem??ll??",
                "miljoonalta "
                "kahdeltasadaltakolmeltakymmenelt??nelj??lt??tuhannelta "
                "viidelt??sadaltakuudeltakymmenelt??seitsem??lt??",
                "miljoonalle "
                "kahdellesadallekolmellekymmenellenelj??lletuhannelle "
                "viidellesadallekuudellekymmenelleseitsem??lle",
                "miljoonana "
                "kahtenasatanakolmenakymmenen??nelj??n??tuhantena "
                "viiten??satanakuutenakymmenen??seitsem??n??",
                "miljoonaksi "
                "kahdeksisadaksikolmeksikymmeneksinelj??ksituhanneksi "
                "viideksisadaksikuudeksikymmeneksiseitsem??ksi",
                "miljoonin "
                "kaksinsadoinkolmenkymmeninneljintuhansin "
                "viisinsadoinkuusinkymmeninseitsemin",
                "miljoonatta "
                "kahdettasadattakolmettakymmenett??nelj??tt??tuhannetta "
                "viidett??sadattakuudettakymmenett??seitsem??tt??",
                "miljoonine "
                "kaksinesatoinekolminekymmenineneljinetuhansine "
                "viisinesatoinekuusinekymmenineseitsemine"
            )
        )
        self.assertEqual(
            tuple(n2f(1234567, to="cardinal", case=c, plural=True)
                  for c in CASES),
            (
                "miljoonat "
                "kahdetsadatkolmetkymmenetnelj??ttuhannet "
                "viidetsadatkuudetkymmenetseitsem??t",
                "miljoonien "
                "kaksiensatojenkolmienkymmenienneljientuhansien "
                "viisiensatojenkuusienkymmenienseitsemien",
                "miljoonia "
                "kaksiasatojakolmiakymmeni??nelji??tuhansia "
                "viisi??satojakuusiakymmeni??seitsemi??",
                "miljoonissa "
                "kaksissasadoissakolmissakymmeniss??neljiss??tuhansissa "
                "viisiss??sadoissakuusissakymmeniss??seitsemiss??",
                "miljoonista "
                "kaksistasadoistakolmistakymmenist??neljist??tuhansista "
                "viisist??sadoistakuusistakymmenist??seitsemist??",
                "miljooniin "
                "kaksiinsatoihinkolmiinkymmeniinneljiintuhansiin "
                "viisiinsatoihinkuusiinkymmeniinseitsemiin",
                "miljoonilla "
                "kaksillasadoillakolmillakymmenill??neljill??tuhansilla "
                "viisill??sadoillakuusillakymmenill??seitsemill??",
                "miljoonilta "
                "kaksiltasadoiltakolmiltakymmenilt??neljilt??tuhansilta "
                "viisilt??sadoiltakuusiltakymmenilt??seitsemilt??",
                "miljoonille "
                "kaksillesadoillekolmillekymmenilleneljilletuhansille "
                "viisillesadoillekuusillekymmenilleseitsemille",
                "miljoonina "
                "kaksinasatoinakolminakymmenin??neljin??tuhansina "
                "viisin??satoinakuusinakymmenin??seitsemin??",
                "miljooniksi "
                "kaksiksisadoiksikolmiksikymmeniksineljiksituhansiksi "
                "viisiksisadoiksikuusiksikymmeniksiseitsemiksi",
                "miljoonin "
                "kaksinsadoinkolminkymmeninneljintuhansin "
                "viisinsadoinkuusinkymmeninseitsemin",
                "miljoonitta "
                "kaksittasadoittakolmittakymmenitt??neljitt??tuhansitta "
                "viisitt??sadoittakuusittakymmenitt??seitsemitt??",
                "miljoonine "
                "kaksinesatoinekolminekymmenineneljinetuhansine "
                "viisinesatoinekuusinekymmenineseitsemine"
            )
        )

        # one billion (short scale)
        self.assertEqual(
            tuple(n2f(10**9, to="cardinal", case=c) for c in CASES),
            ("miljardi", "miljardin", "miljardia",
             "miljardissa", "miljardista", "miljardiin",
             "miljardilla", "miljardilta", "miljardille",
             "miljardina", "miljardiksi",
             "miljardein", "miljarditta", "miljardeine")
        )
        self.assertEqual(
            tuple(n2f(10**9, to="cardinal", case=c, plural=True)
                  for c in CASES),
            ("miljardit", "miljardien", "miljardeja",
             "miljardeissa", "miljardeista", "miljardeihin",
             "miljardeilla", "miljardeilta", "miljardeille",
             "miljardeina", "miljardeiksi",
             "miljardein", "miljardeitta", "miljardeine")
        )

        # one billion, two hundred and thirty-four million,
        # five hundred and sixty-seven thousand, eight hundred and ninety
        # (short scale)
        self.assertEqual(
            tuple(n2f(1234567890, to="cardinal", case=c) for c in CASES),
            (
                "miljardi "
                "kaksisataakolmekymment??nelj??miljoonaa "
                "viisisataakuusikymment??seitsem??ntuhatta "
                "kahdeksansataayhdeks??nkymment??",
                "miljardin "
                "kahdensadankolmenkymmenennelj??nmiljoonan "
                "viidensadankuudenkymmenenseitsem??ntuhannen "
                "kahdeksansadanyhdeks??nkymmenen",
                "miljardia "
                "kahtasataakolmeakymment??nelj????miljoonaa "
                "viitt??sataakuuttakymment??seitsem????tuhatta "
                "kahdeksaasataayhdeks????kymment??",
                "miljardissa "
                "kahdessasadassakolmessakymmeness??nelj??ss??miljoonassa "
                "viidess??sadassakuudessakymmeness??seitsem??ss??tuhannessa "
                "kahdeksassasadassayhdeks??ss??kymmeness??",
                "miljardista "
                "kahdestasadastakolmestakymmenest??nelj??st??miljoonasta "
                "viidest??sadastakuudestakymmenest??seitsem??st??tuhannesta "
                "kahdeksastasadastayhdeks??st??kymmenest??",
                "miljardiin "
                "kahteensataankolmeenkymmeneennelj????nmiljoonaan "
                "viiteensataankuuteenkymmeneenseitsem????ntuhanteen "
                "kahdeksaansataanyhdeks????nkymmeneen",
                "miljardilla "
                "kahdellasadallakolmellakymmenell??nelj??ll??miljoonalla "
                "viidell??sadallakuudellakymmenell??seitsem??ll??tuhannella "
                "kahdeksallasadallayhdeks??ll??kymmenell??",
                "miljardilta "
                "kahdeltasadaltakolmeltakymmenelt??nelj??lt??miljoonalta "
                "viidelt??sadaltakuudeltakymmenelt??seitsem??lt??tuhannelta "
                "kahdeksaltasadaltayhdeks??lt??kymmenelt??",
                "miljardille "
                "kahdellesadallekolmellekymmenellenelj??llemiljoonalle "
                "viidellesadallekuudellekymmenelleseitsem??lletuhannelle "
                "kahdeksallesadalleyhdeks??llekymmenelle",
                "miljardina "
                "kahtenasatanakolmenakymmenen??nelj??n??miljoonana "
                "viiten??satanakuutenakymmenen??seitsem??n??tuhantena "
                "kahdeksanasatanayhdeks??n??kymmenen??",
                "miljardiksi "
                "kahdeksisadaksikolmeksikymmeneksinelj??ksimiljoonaksi "
                "viideksisadaksikuudeksikymmeneksiseitsem??ksituhanneksi "
                "kahdeksaksisadaksiyhdeks??ksikymmeneksi",
                "miljardein "
                "kaksinsadoinkolmenkymmeninneljinmiljoonin "
                "viisinsadoinkuusinkymmeninseitsemintuhansin "
                "kahdeksinsadoinyhdeksinkymmenin",
                "miljarditta "
                "kahdettasadattakolmettakymmenett??nelj??tt??miljoonatta "
                "viidett??sadattakuudettakymmenett??seitsem??tt??tuhannetta "
                "kahdeksattasadattayhdeks??tt??kymmenett??",
                "miljardeine "
                "kaksinesatoinekolminekymmenineneljinemiljoonine "
                "viisinesatoinekuusinekymmenineseitseminetuhansine "
                "kahdeksinesatoineyhdeksinekymmenine"
            )
        )
        self.assertEqual(
            tuple(n2f(1234567890, to="cardinal", case=c, plural=True)
                  for c in CASES),
            (
                "miljardit "
                "kahdetsadatkolmetkymmenetnelj??tmiljoonat "
                "viidetsadatkuudetkymmenetseitsem??ttuhannet "
                "kahdeksatsadatyhdeks??tkymmenet",
                "miljardien "
                "kaksiensatojenkolmienkymmenienneljienmiljoonien "
                "viisiensatojenkuusienkymmenienseitsemientuhansien "
                "kahdeksiensatojenyhdeksienkymmenien",
                "miljardeja "
                "kaksiasatojakolmiakymmeni??nelji??miljoonia "
                "viisi??satojakuusiakymmeni??seitsemi??tuhansia "
                "kahdeksiasatojayhdeksi??kymmeni??",
                "miljardeissa "
                "kaksissasadoissakolmissakymmeniss??neljiss??miljoonissa "
                "viisiss??sadoissakuusissakymmeniss??seitsemiss??tuhansissa "
                "kahdeksissasadoissayhdeksiss??kymmeniss??",
                "miljardeista "
                "kaksistasadoistakolmistakymmenist??neljist??miljoonista "
                "viisist??sadoistakuusistakymmenist??seitsemist??tuhansista "
                "kahdeksistasadoistayhdeksist??kymmenist??",
                "miljardeihin "
                "kaksiinsatoihinkolmiinkymmeniinneljiinmiljooniin "
                "viisiinsatoihinkuusiinkymmeniinseitsemiintuhansiin "
                "kahdeksiinsatoihinyhdeksiinkymmeniin",
                "miljardeilla "
                "kaksillasadoillakolmillakymmenill??neljill??miljoonilla "
                "viisill??sadoillakuusillakymmenill??seitsemill??tuhansilla "
                "kahdeksillasadoillayhdeksill??kymmenill??",
                "miljardeilta "
                "kaksiltasadoiltakolmiltakymmenilt??neljilt??miljoonilta "
                "viisilt??sadoiltakuusiltakymmenilt??seitsemilt??tuhansilta "
                "kahdeksiltasadoiltayhdeksilt??kymmenilt??",
                "miljardeille "
                "kaksillesadoillekolmillekymmenilleneljillemiljoonille "
                "viisillesadoillekuusillekymmenilleseitsemilletuhansille "
                "kahdeksillesadoilleyhdeksillekymmenille",
                "miljardeina "
                "kaksinasatoinakolminakymmenin??neljin??miljoonina "
                "viisin??satoinakuusinakymmenin??seitsemin??tuhansina "
                "kahdeksinasatoinayhdeksin??kymmenin??",
                "miljardeiksi "
                "kaksiksisadoiksikolmiksikymmeniksineljiksimiljooniksi "
                "viisiksisadoiksikuusiksikymmeniksiseitsemiksituhansiksi "
                "kahdeksiksisadoiksiyhdeksiksikymmeniksi",
                "miljardein "
                "kaksinsadoinkolminkymmeninneljinmiljoonin "
                "viisinsadoinkuusinkymmeninseitsemintuhansin "
                "kahdeksinsadoinyhdeksinkymmenin",
                "miljardeitta "
                "kaksittasadoittakolmittakymmenitt??neljitt??miljoonitta "
                "viisitt??sadoittakuusittakymmenitt??seitsemitt??tuhansitta "
                "kahdeksittasadoittayhdeksitt??kymmenitt??",
                "miljardeine "
                "kaksinesatoinekolminekymmenineneljinemiljoonine "
                "viisinesatoinekuusinekymmenineseitseminetuhansine "
                "kahdeksinesatoineyhdeksinekymmenine"
            )
        )

        # one trillion (short scale)
        self.assertEqual(
            tuple(n2f((10**6)**2, to="cardinal", case=c) for c in CASES),
            ("biljoona", "biljoonan", "biljoonaa",
             "biljoonassa", "biljoonasta", "biljoonaan",
             "biljoonalla", "biljoonalta", "biljoonalle",
             "biljoonana", "biljoonaksi",
             "biljoonin", "biljoonatta", "biljoonine")
        )
        self.assertEqual(
            tuple(n2f((10**6)**2, to="cardinal", case=c, plural=True)
                  for c in CASES),
            ("biljoonat", "biljoonien", "biljoonia",
             "biljoonissa", "biljoonista", "biljooniin",
             "biljoonilla", "biljoonilta", "biljoonille",
             "biljoonina", "biljooniksi",
             "biljoonin", "biljoonitta", "biljoonine")
        )

        # one quintillion (short scale)
        self.assertEqual(
            tuple(n2f((10**6)**3, to="cardinal", case=c) for c in CASES),
            ("triljoona", "triljoonan", "triljoonaa",
             "triljoonassa", "triljoonasta", "triljoonaan",
             "triljoonalla", "triljoonalta", "triljoonalle",
             "triljoonana", "triljoonaksi",
             "triljoonin", "triljoonatta", "triljoonine")
        )
        self.assertEqual(
            tuple(n2f((10**6)**3, to="cardinal", case=c, plural=True)
                  for c in CASES),
            ("triljoonat", "triljoonien", "triljoonia",
             "triljoonissa", "triljoonista", "triljooniin",
             "triljoonilla", "triljoonilta", "triljoonille",
             "triljoonina", "triljooniksi",
             "triljoonin", "triljoonitta", "triljoonine")
        )

    def test_high_ord(self):

        # ten thousand
        self.assertEqual(
            tuple(n2f(10000, to="ordinal", case=c) for c in CASES),
            (
                "kymmenestuhannes",
                "kymmenennentuhannennen",
                "kymmenett??tuhannetta",
                "kymmenenness??tuhannennessa",
                "kymmenennest??tuhannennesta",
                "kymmenenteentuhannenteen",
                "kymmenennell??tuhannennella",
                "kymmenennelt??tuhannennelta",
                "kymmenennelletuhannennelle",
                "kymmenenten??tuhannentena",
                "kymmenenneksituhannenneksi",
                "kymmenensintuhannensin",
                "kymmenennett??tuhannennetta",
                "kymmenensinetuhannensine"
            )
        )
        self.assertEqual(
            tuple(n2f(10000, to="ordinal", case=c, plural=True)
                  for c in CASES),
            (
                "kymmenennettuhannennet",
                "kymmenensientuhannensien",
                "kymmenensi??tuhannensia",
                "kymmenensiss??tuhannensissa",
                "kymmenensist??tuhannensista",
                "kymmenensiintuhannensiin",
                "kymmenensill??tuhannensilla",
                "kymmenensilt??tuhannensilta",
                "kymmenensilletuhannensille",
                "kymmenensin??tuhannensina",
                "kymmenensiksituhannensiksi",
                "kymmenensintuhannensin",
                "kymmenensitt??tuhannensitta",
                "kymmenensinetuhannensine"
            )
        )

        # twelve thousand, three hundred and forty-five
        self.assertEqual(
            tuple(n2f(12345, to="ordinal", case=c) for c in CASES),
            (
                "kahdestoistatuhannes "
                "kolmassadasnelj??skymmenesviides",
                "kahdennentoistatuhannennen "
                "kolmannensadannennelj??nnenkymmenennenviidennen",
                "kahdettatoistatuhannetta "
                "kolmattasadattanelj??tt??kymmenett??viidett??",
                "kahdennessatoistatuhannennessa "
                "kolmannessasadannessanelj??nness??kymmenenness??viidenness??",
                "kahdennestatoistatuhannennesta "
                "kolmannestasadannestanelj??nnest??kymmenennest??viidennest??",
                "kahdenteentoistatuhannenteen "
                "kolmanteensadanteennelj??nteenkymmenenteenviidenteen",
                "kahdennellatoistatuhannennella "
                "kolmannellasadannellanelj??nnell??kymmenennell??viidennell??",
                "kahdenneltatoistatuhannennelta "
                "kolmanneltasadanneltanelj??nnelt??kymmenennelt??viidennelt??",
                "kahdennelletoistatuhannennelle "
                "kolmannellesadannellenelj??nnellekymmenennelleviidennelle",
                "kahdentenatoistatuhannentena "
                "kolmantenasadantenanelj??nten??kymmenenten??viidenten??",
                "kahdenneksitoistatuhannenneksi "
                "kolmanneksisadanneksinelj??nneksikymmenenneksiviidenneksi",
                "kahdensintoistatuhannensin "
                "kolmansinsadansinnelj??nsinkymmenensinviidensin",
                "kahdennettatoistatuhannennetta "
                "kolmannettasadannettanelj??nnett??kymmenennett??viidennett??",
                "kahdensinetoistatuhannensine "
                "kolmansinesadansinenelj??nsinekymmenensineviidensine"
            )
        )
        self.assertEqual(
            tuple(n2f(12345, to="ordinal", case=c, plural=True)
                  for c in CASES),
            (
                "kahdennettoistatuhannennet "
                "kolmannetsadannetnelj??nnetkymmenennetviidennet",
                "kahdensientoistatuhannensien "
                "kolmansiensadansiennelj??nsienkymmenensienviidensien",
                "kahdensiatoistatuhannensia "
                "kolmansiasadansianelj??nsi??kymmenensi??viidensi??",
                "kahdensissatoistatuhannensissa "
                "kolmansissasadansissanelj??nsiss??kymmenensiss??viidensiss??",
                "kahdensistatoistatuhannensista "
                "kolmansistasadansistanelj??nsist??kymmenensist??viidensist??",
                "kahdensiintoistatuhannensiin "
                "kolmansiinsadansiinnelj??nsiinkymmenensiinviidensiin",
                "kahdensillatoistatuhannensilla "
                "kolmansillasadansillanelj??nsill??kymmenensill??viidensill??",
                "kahdensiltatoistatuhannensilta "
                "kolmansiltasadansiltanelj??nsilt??kymmenensilt??viidensilt??",
                "kahdensilletoistatuhannensille "
                "kolmansillesadansillenelj??nsillekymmenensilleviidensille",
                "kahdensinatoistatuhannensina "
                "kolmansinasadansinanelj??nsin??kymmenensin??viidensin??",
                "kahdensiksitoistatuhannensiksi "
                "kolmansiksisadansiksinelj??nsiksikymmenensiksiviidensiksi",
                "kahdensintoistatuhannensin "
                "kolmansinsadansinnelj??nsinkymmenensinviidensin",
                "kahdensittatoistatuhannensitta "
                "kolmansittasadansittanelj??nsitt??kymmenensitt??viidensitt??",
                "kahdensinetoistatuhannensine "
                "kolmansinesadansinenelj??nsinekymmenensineviidensine"
            )
        )

        # one hundred thousand
        self.assertEqual(
            tuple(n2f(100000, to="ordinal", case=c) for c in CASES),
            (
                "sadastuhannes",
                "sadannentuhannennen",
                "sadattatuhannetta",
                "sadannessatuhannennessa",
                "sadannestatuhannennesta",
                "sadanteentuhannenteen",
                "sadannellatuhannennella",
                "sadanneltatuhannennelta",
                "sadannelletuhannennelle",
                "sadantenatuhannentena",
                "sadanneksituhannenneksi",
                "sadansintuhannensin",
                "sadannettatuhannennetta",
                "sadansinetuhannensine"
            )
        )
        self.assertEqual(
            tuple(n2f(100000, to="ordinal", case=c, plural=True)
                  for c in CASES),
            (
                "sadannettuhannennet",
                "sadansientuhannensien",
                "sadansiatuhannensia",
                "sadansissatuhannensissa",
                "sadansistatuhannensista",
                "sadansiintuhannensiin",
                "sadansillatuhannensilla",
                "sadansiltatuhannensilta",
                "sadansilletuhannensille",
                "sadansinatuhannensina",
                "sadansiksituhannensiksi",
                "sadansintuhannensin",
                "sadansittatuhannensitta",
                "sadansinetuhannensine"
            )
        )

        # one hundred and twenty-three thousand, four hundred and fifty-six
        self.assertEqual(
            tuple(n2f(123456, to="ordinal", case=c) for c in CASES),
            (
                "sadaskahdeskymmeneskolmastuhannes "
                "nelj??ssadasviideskymmeneskuudes",
                "sadannenkahdennenkymmenennenkolmannentuhannennen "
                "nelj??nnensadannenviidennenkymmenennenkuudennen",
                "sadattakahdettakymmenett??kolmattatuhannetta "
                "nelj??tt??sadattaviidett??kymmenett??kuudetta",
                "sadannessakahdennessakymmenenness??kolmannessatuhannennessa "
                "nelj??nness??sadannessaviidenness??kymmenenness??kuudennessa",
                "sadannestakahdennestakymmenennest??kolmannestatuhannennesta "
                "nelj??nnest??sadannestaviidennest??kymmenennest??kuudennesta",
                "sadanteenkahdenteenkymmenenteenkolmanteentuhannenteen "
                "nelj??nteensadanteenviidenteenkymmenenteenkuudenteen",
                "sadannellakahdennellakymmenennell??kolmannellatuhannennella "
                "nelj??nnell??sadannellaviidennell??kymmenennell??kuudennella",
                "sadanneltakahdenneltakymmenennelt??kolmanneltatuhannennelta "
                "nelj??nnelt??sadanneltaviidennelt??kymmenennelt??kuudennelta",
                "sadannellekahdennellekymmenennellekolmannelletuhannennelle "
                "nelj??nnellesadannelleviidennellekymmenennellekuudennelle",
                "sadantenakahdentenakymmenenten??kolmantenatuhannentena "
                "nelj??nten??sadantenaviidenten??kymmenenten??kuudentena",
                "sadanneksikahdenneksikymmenenneksikolmanneksituhannenneksi "
                "nelj??nneksisadanneksiviidenneksikymmenenneksikuudenneksi",
                "sadansinkahdensinkymmenensinkolmansintuhannensin "
                "nelj??nsinsadansinviidensinkymmenensinkuudensin",
                "sadannettakahdennettakymmenennett??kolmannettatuhannennetta "
                "nelj??nnett??sadannettaviidennett??kymmenennett??kuudennetta",
                "sadansinekahdensinekymmenensinekolmansinetuhannensine "
                "nelj??nsinesadansineviidensinekymmenensinekuudensine"
            )
        )
        self.assertEqual(
            tuple(n2f(123456, to="ordinal", case=c, plural=True)
                  for c in CASES),
            (
                "sadannetkahdennetkymmenennetkolmannettuhannennet "
                "nelj??nnetsadannetviidennetkymmenennetkuudennet",
                "sadansienkahdensienkymmenensienkolmansientuhannensien "
                "nelj??nsiensadansienviidensienkymmenensienkuudensien",
                "sadansiakahdensiakymmenensi??kolmansiatuhannensia "
                "nelj??nsi??sadansiaviidensi??kymmenensi??kuudensia",
                "sadansissakahdensissakymmenensiss??kolmansissatuhannensissa "
                "nelj??nsiss??sadansissaviidensiss??kymmenensiss??kuudensissa",
                "sadansistakahdensistakymmenensist??kolmansistatuhannensista "
                "nelj??nsist??sadansistaviidensist??kymmenensist??kuudensista",
                "sadansiinkahdensiinkymmenensiinkolmansiintuhannensiin "
                "nelj??nsiinsadansiinviidensiinkymmenensiinkuudensiin",
                "sadansillakahdensillakymmenensill??kolmansillatuhannensilla "
                "nelj??nsill??sadansillaviidensill??kymmenensill??kuudensilla",
                "sadansiltakahdensiltakymmenensilt??kolmansiltatuhannensilta "
                "nelj??nsilt??sadansiltaviidensilt??kymmenensilt??kuudensilta",
                "sadansillekahdensillekymmenensillekolmansilletuhannensille "
                "nelj??nsillesadansilleviidensillekymmenensillekuudensille",
                "sadansinakahdensinakymmenensin??kolmansinatuhannensina "
                "nelj??nsin??sadansinaviidensin??kymmenensin??kuudensina",
                "sadansiksikahdensiksikymmenensiksikolmansiksituhannensiksi "
                "nelj??nsiksisadansiksiviidensiksikymmenensiksikuudensiksi",
                "sadansinkahdensinkymmenensinkolmansintuhannensin "
                "nelj??nsinsadansinviidensinkymmenensinkuudensin",
                "sadansittakahdensittakymmenensitt??kolmansittatuhannensitta "
                "nelj??nsitt??sadansittaviidensitt??kymmenensitt??kuudensitta",
                "sadansinekahdensinekymmenensinekolmansinetuhannensine "
                "nelj??nsinesadansineviidensinekymmenensinekuudensine"
            )
        )

        # one million
        self.assertEqual(
            tuple(n2f(10**6, to="ordinal", case=c) for c in CASES),
            ("miljoonas", "miljoonannen", "miljoonatta",
             "miljoonannessa", "miljoonannesta", "miljoonanteen",
             "miljoonannella", "miljoonannelta", "miljoonannelle",
             "miljoonantena", "miljoonanneksi",
             "miljoonansin", "miljoonannetta", "miljoonansine")
        )
        self.assertEqual(
            tuple(n2f(10**6, to="ordinal", case=c, plural=True)
                  for c in CASES),
            ("miljoonannet", "miljoonansien", "miljoonansia",
             "miljoonansissa", "miljoonansista", "miljoonansiin",
             "miljoonansilla", "miljoonansilta", "miljoonansille",
             "miljoonansina", "miljoonansiksi",
             "miljoonansin", "miljoonansitta", "miljoonansine")
        )

        # one million, two hundred and thirty-four thousand,
        # five hundred and sixty-seven
        self.assertEqual(
            tuple(n2f(1234567, to="ordinal", case=c) for c in CASES),
            (
                "miljoonas "
                "kahdessadaskolmaskymmenesnelj??s"
                "tuhannes "
                "viidessadaskuudeskymmenesseitsem??s",
                "miljoonannen "
                "kahdennensadannenkolmannenkymmenennennelj??nnen"
                "tuhannennen "
                "viidennensadannenkuudennenkymmenennenseitsem??nnen",
                "miljoonatta "
                "kahdettasadattakolmattakymmenett??nelj??tt??"
                "tuhannetta "
                "viidett??sadattakuudettakymmenett??seitsem??tt??",
                "miljoonannessa "
                "kahdennessasadannessakolmannessakymmenenness??nelj??nness??"
                "tuhannennessa "
                "viidenness??sadannessakuudennessakymmenenness??seitsem??nness??",
                "miljoonannesta "
                "kahdennestasadannestakolmannestakymmenennest??nelj??nnest??"
                "tuhannennesta "
                "viidennest??sadannestakuudennestakymmenennest??seitsem??nnest??",
                "miljoonanteen "
                "kahdenteensadanteenkolmanteenkymmenenteennelj??nteen"
                "tuhannenteen "
                "viidenteensadanteenkuudenteenkymmenenteenseitsem??nteen",
                "miljoonannella "
                "kahdennellasadannellakolmannellakymmenennell??nelj??nnell??"
                "tuhannennella "
                "viidennell??sadannellakuudennellakymmenennell??seitsem??nnell??",
                "miljoonannelta "
                "kahdenneltasadanneltakolmanneltakymmenennelt??nelj??nnelt??"
                "tuhannennelta "
                "viidennelt??sadanneltakuudenneltakymmenennelt??seitsem??nnelt??",
                "miljoonannelle "
                "kahdennellesadannellekolmannellekymmenennellenelj??nnelle"
                "tuhannennelle "
                "viidennellesadannellekuudennellekymmenennelleseitsem??nnelle",
                "miljoonantena "
                "kahdentenasadantenakolmantenakymmenenten??nelj??nten??"
                "tuhannentena "
                "viidenten??sadantenakuudentenakymmenenten??seitsem??nten??",
                "miljoonanneksi "
                "kahdenneksisadanneksikolmanneksikymmenenneksinelj??nneksi"
                "tuhannenneksi "
                "viidenneksisadanneksikuudenneksikymmenenneksiseitsem??nneksi",
                "miljoonansin "
                "kahdensinsadansinkolmansinkymmenensinnelj??nsin"
                "tuhannensin "
                "viidensinsadansinkuudensinkymmenensinseitsem??nsin",
                "miljoonannetta "
                "kahdennettasadannettakolmannettakymmenennett??nelj??nnett??"
                "tuhannennetta "
                "viidennett??sadannettakuudennettakymmenennett??seitsem??nnett??",
                "miljoonansine "
                "kahdensinesadansinekolmansinekymmenensinenelj??nsine"
                "tuhannensine "
                "viidensinesadansinekuudensinekymmenensineseitsem??nsine"
            )
        )
        self.assertEqual(
            tuple(n2f(1234567, to="ordinal", case=c, plural=True)
                  for c in CASES),
            (
                "miljoonannet "
                "kahdennetsadannetkolmannetkymmenennetnelj??nnet"
                "tuhannennet "
                "viidennetsadannetkuudennetkymmenennetseitsem??nnet",
                "miljoonansien "
                "kahdensiensadansienkolmansienkymmenensiennelj??nsien"
                "tuhannensien "
                "viidensiensadansienkuudensienkymmenensienseitsem??nsien",
                "miljoonansia "
                "kahdensiasadansiakolmansiakymmenensi??nelj??nsi??"
                "tuhannensia "
                "viidensi??sadansiakuudensiakymmenensi??seitsem??nsi??",
                "miljoonansissa "
                "kahdensissasadansissakolmansissakymmenensiss??nelj??nsiss??"
                "tuhannensissa "
                "viidensiss??sadansissakuudensissakymmenensiss??seitsem??nsiss??",
                "miljoonansista "
                "kahdensistasadansistakolmansistakymmenensist??nelj??nsist??"
                "tuhannensista "
                "viidensist??sadansistakuudensistakymmenensist??seitsem??nsist??",
                "miljoonansiin "
                "kahdensiinsadansiinkolmansiinkymmenensiinnelj??nsiin"
                "tuhannensiin "
                "viidensiinsadansiinkuudensiinkymmenensiinseitsem??nsiin",
                "miljoonansilla "
                "kahdensillasadansillakolmansillakymmenensill??nelj??nsill??"
                "tuhannensilla "
                "viidensill??sadansillakuudensillakymmenensill??seitsem??nsill??",
                "miljoonansilta "
                "kahdensiltasadansiltakolmansiltakymmenensilt??nelj??nsilt??"
                "tuhannensilta "
                "viidensilt??sadansiltakuudensiltakymmenensilt??seitsem??nsilt??",
                "miljoonansille "
                "kahdensillesadansillekolmansillekymmenensillenelj??nsille"
                "tuhannensille "
                "viidensillesadansillekuudensillekymmenensilleseitsem??nsille",
                "miljoonansina "
                "kahdensinasadansinakolmansinakymmenensin??nelj??nsin??"
                "tuhannensina "
                "viidensin??sadansinakuudensinakymmenensin??seitsem??nsin??",
                "miljoonansiksi "
                "kahdensiksisadansiksikolmansiksikymmenensiksinelj??nsiksi"
                "tuhannensiksi "
                "viidensiksisadansiksikuudensiksikymmenensiksiseitsem??nsiksi",
                "miljoonansin "
                "kahdensinsadansinkolmansinkymmenensinnelj??nsin"
                "tuhannensin "
                "viidensinsadansinkuudensinkymmenensinseitsem??nsin",
                "miljoonansitta "
                "kahdensittasadansittakolmansittakymmenensitt??nelj??nsitt??"
                "tuhannensitta "
                "viidensitt??sadansittakuudensittakymmenensitt??seitsem??nsitt??",
                "miljoonansine "
                "kahdensinesadansinekolmansinekymmenensinenelj??nsine"
                "tuhannensine "
                "viidensinesadansinekuudensinekymmenensineseitsem??nsine"
            )
        )

        # one billion (short scale)
        self.assertEqual(
            tuple(n2f(10**9, to="ordinal", case=c) for c in CASES),
            ("miljardis", "miljardinnen", "miljarditta",
             "miljardinnessa", "miljardinnesta", "miljardinteen",
             "miljardinnella", "miljardinnelta", "miljardinnelle",
             "miljardintena", "miljardinneksi",
             "miljardinsin", "miljardinnetta", "miljardinsine")
        )
        self.assertEqual(
            tuple(n2f(10**9, to="ordinal", case=c, plural=True)
                  for c in CASES),
            ("miljardinnet", "miljardinsien", "miljardinsia",
             "miljardinsissa", "miljardinsista", "miljardinsiin",
             "miljardinsilla", "miljardinsilta", "miljardinsille",
             "miljardinsina", "miljardinsiksi",
             "miljardinsin", "miljardinsitta", "miljardinsine")
        )

        # one billion, two hundred and thirty-four million,
        # five hundred and sixty-seven thousand, eight hundred and ninety
        # (short scale)
        self.assertEqual(
            tuple(n2f(1234567890, to="ordinal", case=c) for c in CASES),
            (
                "miljardis "
                "kahdessadaskolmaskymmenesnelj??s"
                "miljoonas "
                "viidessadaskuudeskymmenesseitsem??s"
                "tuhannes "
                "kahdeksassadasyhdeks??skymmenes",
                "miljardinnen "
                "kahdennensadannenkolmannenkymmenennennelj??nnen"
                "miljoonannen "
                "viidennensadannenkuudennenkymmenennenseitsem??nnen"
                "tuhannennen "
                "kahdeksannensadannenyhdeks??nnenkymmenennen",
                "miljarditta "
                "kahdettasadattakolmattakymmenett??nelj??tt??"
                "miljoonatta "
                "viidett??sadattakuudettakymmenett??seitsem??tt??"
                "tuhannetta "
                "kahdeksattasadattayhdeks??tt??kymmenett??",
                "miljardinnessa "
                "kahdennessasadannessakolmannessakymmenenness??nelj??nness??"
                "miljoonannessa "
                "viidenness??sadannessakuudennessakymmenenness??seitsem??nness??"
                "tuhannennessa "
                "kahdeksannessasadannessayhdeks??nness??kymmenenness??",
                "miljardinnesta "
                "kahdennestasadannestakolmannestakymmenennest??nelj??nnest??"
                "miljoonannesta "
                "viidennest??sadannestakuudennestakymmenennest??seitsem??nnest??"
                "tuhannennesta "
                "kahdeksannestasadannestayhdeks??nnest??kymmenennest??",
                "miljardinteen "
                "kahdenteensadanteenkolmanteenkymmenenteennelj??nteen"
                "miljoonanteen "
                "viidenteensadanteenkuudenteenkymmenenteenseitsem??nteen"
                "tuhannenteen "
                "kahdeksanteensadanteenyhdeks??nteenkymmenenteen",
                "miljardinnella "
                "kahdennellasadannellakolmannellakymmenennell??nelj??nnell??"
                "miljoonannella "
                "viidennell??sadannellakuudennellakymmenennell??seitsem??nnell??"
                "tuhannennella "
                "kahdeksannellasadannellayhdeks??nnell??kymmenennell??",
                "miljardinnelta "
                "kahdenneltasadanneltakolmanneltakymmenennelt??nelj??nnelt??"
                "miljoonannelta "
                "viidennelt??sadanneltakuudenneltakymmenennelt??seitsem??nnelt??"
                "tuhannennelta "
                "kahdeksanneltasadanneltayhdeks??nnelt??kymmenennelt??",
                "miljardinnelle "
                "kahdennellesadannellekolmannellekymmenennellenelj??nnelle"
                "miljoonannelle "
                "viidennellesadannellekuudennellekymmenennelleseitsem??nnelle"
                "tuhannennelle "
                "kahdeksannellesadannelleyhdeks??nnellekymmenennelle",
                "miljardintena "
                "kahdentenasadantenakolmantenakymmenenten??nelj??nten??"
                "miljoonantena "
                "viidenten??sadantenakuudentenakymmenenten??seitsem??nten??"
                "tuhannentena "
                "kahdeksantenasadantenayhdeks??nten??kymmenenten??",
                "miljardinneksi "
                "kahdenneksisadanneksikolmanneksikymmenenneksinelj??nneksi"
                "miljoonanneksi "
                "viidenneksisadanneksikuudenneksikymmenenneksiseitsem??nneksi"
                "tuhannenneksi "
                "kahdeksanneksisadanneksiyhdeks??nneksikymmenenneksi",
                "miljardinsin "
                "kahdensinsadansinkolmansinkymmenensinnelj??nsin"
                "miljoonansin "
                "viidensinsadansinkuudensinkymmenensinseitsem??nsin"
                "tuhannensin "
                "kahdeksansinsadansinyhdeks??nsinkymmenensin",
                "miljardinnetta "
                "kahdennettasadannettakolmannettakymmenennett??nelj??nnett??"
                "miljoonannetta "
                "viidennett??sadannettakuudennettakymmenennett??seitsem??nnett??"
                "tuhannennetta "
                "kahdeksannettasadannettayhdeks??nnett??kymmenennett??",
                "miljardinsine "
                "kahdensinesadansinekolmansinekymmenensinenelj??nsine"
                "miljoonansine "
                "viidensinesadansinekuudensinekymmenensineseitsem??nsine"
                "tuhannensine "
                "kahdeksansinesadansineyhdeks??nsinekymmenensine"
            )
        )
        self.assertEqual(
            tuple(n2f(1234567890, to="ordinal", case=c, plural=True)
                  for c in CASES),
            (
                "miljardinnet "
                "kahdennetsadannetkolmannetkymmenennetnelj??nnet"
                "miljoonannet "
                "viidennetsadannetkuudennetkymmenennetseitsem??nnet"
                "tuhannennet "
                "kahdeksannetsadannetyhdeks??nnetkymmenennet",
                "miljardinsien "
                "kahdensiensadansienkolmansienkymmenensiennelj??nsien"
                "miljoonansien "
                "viidensiensadansienkuudensienkymmenensienseitsem??nsien"
                "tuhannensien "
                "kahdeksansiensadansienyhdeks??nsienkymmenensien",
                "miljardinsia "
                "kahdensiasadansiakolmansiakymmenensi??nelj??nsi??"
                "miljoonansia "
                "viidensi??sadansiakuudensiakymmenensi??seitsem??nsi??"
                "tuhannensia "
                "kahdeksansiasadansiayhdeks??nsi??kymmenensi??",
                "miljardinsissa "
                "kahdensissasadansissakolmansissakymmenensiss??nelj??nsiss??"
                "miljoonansissa "
                "viidensiss??sadansissakuudensissakymmenensiss??seitsem??nsiss??"
                "tuhannensissa "
                "kahdeksansissasadansissayhdeks??nsiss??kymmenensiss??",
                "miljardinsista "
                "kahdensistasadansistakolmansistakymmenensist??nelj??nsist??"
                "miljoonansista "
                "viidensist??sadansistakuudensistakymmenensist??seitsem??nsist??"
                "tuhannensista "
                "kahdeksansistasadansistayhdeks??nsist??kymmenensist??",
                "miljardinsiin "
                "kahdensiinsadansiinkolmansiinkymmenensiinnelj??nsiin"
                "miljoonansiin "
                "viidensiinsadansiinkuudensiinkymmenensiinseitsem??nsiin"
                "tuhannensiin "
                "kahdeksansiinsadansiinyhdeks??nsiinkymmenensiin",
                "miljardinsilla "
                "kahdensillasadansillakolmansillakymmenensill??nelj??nsill??"
                "miljoonansilla "
                "viidensill??sadansillakuudensillakymmenensill??seitsem??nsill??"
                "tuhannensilla "
                "kahdeksansillasadansillayhdeks??nsill??kymmenensill??",
                "miljardinsilta "
                "kahdensiltasadansiltakolmansiltakymmenensilt??nelj??nsilt??"
                "miljoonansilta "
                "viidensilt??sadansiltakuudensiltakymmenensilt??seitsem??nsilt??"
                "tuhannensilta "
                "kahdeksansiltasadansiltayhdeks??nsilt??kymmenensilt??",
                "miljardinsille "
                "kahdensillesadansillekolmansillekymmenensillenelj??nsille"
                "miljoonansille "
                "viidensillesadansillekuudensillekymmenensilleseitsem??nsille"
                "tuhannensille "
                "kahdeksansillesadansilleyhdeks??nsillekymmenensille",
                "miljardinsina "
                "kahdensinasadansinakolmansinakymmenensin??nelj??nsin??"
                "miljoonansina "
                "viidensin??sadansinakuudensinakymmenensin??seitsem??nsin??"
                "tuhannensina "
                "kahdeksansinasadansinayhdeks??nsin??kymmenensin??",
                "miljardinsiksi "
                "kahdensiksisadansiksikolmansiksikymmenensiksinelj??nsiksi"
                "miljoonansiksi "
                "viidensiksisadansiksikuudensiksikymmenensiksiseitsem??nsiksi"
                "tuhannensiksi "
                "kahdeksansiksisadansiksiyhdeks??nsiksikymmenensiksi",
                "miljardinsin "
                "kahdensinsadansinkolmansinkymmenensinnelj??nsin"
                "miljoonansin "
                "viidensinsadansinkuudensinkymmenensinseitsem??nsin"
                "tuhannensin "
                "kahdeksansinsadansinyhdeks??nsinkymmenensin",
                "miljardinsitta "
                "kahdensittasadansittakolmansittakymmenensitt??nelj??nsitt??"
                "miljoonansitta "
                "viidensitt??sadansittakuudensittakymmenensitt??seitsem??nsitt??"
                "tuhannensitta "
                "kahdeksansittasadansittayhdeks??nsitt??kymmenensitt??",
                "miljardinsine "
                "kahdensinesadansinekolmansinekymmenensinenelj??nsine"
                "miljoonansine "
                "viidensinesadansinekuudensinekymmenensineseitsem??nsine"
                "tuhannensine "
                "kahdeksansinesadansineyhdeks??nsinekymmenensine"
            )
        )

        # one trillion (short scale)
        self.assertEqual(
            tuple(n2f((10**6)**2, to="ordinal", case=c) for c in CASES),
            ("biljoonas", "biljoonannen", "biljoonatta",
             "biljoonannessa", "biljoonannesta", "biljoonanteen",
             "biljoonannella", "biljoonannelta", "biljoonannelle",
             "biljoonantena", "biljoonanneksi",
             "biljoonansin", "biljoonannetta", "biljoonansine")
        )
        self.assertEqual(
            tuple(n2f((10**6)**2, to="ordinal", case=c, plural=True)
                  for c in CASES),
            ("biljoonannet", "biljoonansien", "biljoonansia",
             "biljoonansissa", "biljoonansista", "biljoonansiin",
             "biljoonansilla", "biljoonansilta", "biljoonansille",
             "biljoonansina", "biljoonansiksi",
             "biljoonansin", "biljoonansitta", "biljoonansine")
        )

        # one quintillion (short scale)
        self.assertEqual(
            tuple(n2f((10**6)**3, to="ordinal", case=c) for c in CASES),
            ("triljoonas", "triljoonannen", "triljoonatta",
             "triljoonannessa", "triljoonannesta", "triljoonanteen",
             "triljoonannella", "triljoonannelta", "triljoonannelle",
             "triljoonantena", "triljoonanneksi",
             "triljoonansin", "triljoonannetta", "triljoonansine")
        )
        self.assertEqual(
            tuple(n2f((10**6)**3, to="ordinal", case=c, plural=True)
                  for c in CASES),
            ("triljoonannet", "triljoonansien", "triljoonansia",
             "triljoonansissa", "triljoonansista", "triljoonansiin",
             "triljoonansilla", "triljoonansilta", "triljoonansille",
             "triljoonansina", "triljoonansiksi",
             "triljoonansin", "triljoonansitta", "triljoonansine")
        )

    def test_negative(self):
        self.assertEqual(n2f(-1, to="cardinal"), "miinus yksi")
        with self.assertRaises(TypeError):
            n2f(-1, to="ordinal")

    def test_cardinal_float(self):
        self.assertEqual(n2f(1.5, to="cardinal"), "yksi pilkku viisi")
        with self.assertRaises(NotImplementedError):
            n2f(1.5, to="cardinal", case="inessive")

    def test_ordinal_num(self):
        with self.assertRaises(NotImplementedError):
            n2f(1, to="ordinal_num")

    def test_year(self):
        self.assertEqual(n2f(2018, to="year"), "kaksituhattakahdeksantoista")
        self.assertEqual(
            n2f(-99, to="year"),
            "yhdeks??nkymment??yhdeks??n ennen ajanlaskun alkua")

    def test_currency(self):
        self.assertEqual(
            n2f(150, to="currency"), "yksi euro ja viisikymment?? sentti??")
        self.assertEqual(
            n2f(150, to="currency", currency="FIM", adjective=True),
            "yksi Suomen markka ja viisikymment?? penni??")
