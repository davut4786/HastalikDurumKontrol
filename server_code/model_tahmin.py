from ._anvil_designer import Form1Template
from anvil import *

class Form1(Form1Template):
    def __init__(self, **properties):
        self.init_components(**properties)

    def tahmin_et_button_click(self, **event_args):  # Burada click olayı için bir yöntem tanımlıyoruz
        # Kullanıcıdan verileri al
        Tur = self.tur_dropdown.selected_value
        GRAN = self.gran_textbox.text
        GRAN_A = self.gran_a_textbox.text
        LYM = self.lym_textbox.text
        LYM_A = self.lym_a_textbox.text
        MON = self.mon_textbox.text
        HCT = self.hct_textbox.text
        MCH = self.mch_textbox.text
        MCHC = self.mchc_textbox.text
        MCV = self.mcv_textbox.text
        RDW = self.rdw_textbox.text
        WBC = self.wbc_textbox.text
        inkordinasyon = self.inkordinasyon_radio.selected_value
        ishal = self.ishal_radio.selected_value
        istahsizlik = self.istahsizlik_radio.selected_value
        kusma = self.kusma_radio.selected_value
        solunum_guclugu = self.solunum_guclugu_radio.selected_value

        # Model tahmini yapma
        sonuc = anvil.server.call('model_tahmin', [Tur, GRAN, GRAN_A, LYM, LYM_A, MON, HCT, MCH, MCHC, MCV, RDW, WBC, inkordinasyon, ishal, istahsizlik, kusma, solunum_guclugu])

        # Sonucu göster
        self.sonuc_label.text = f"Tahmin Sonucu: {sonuc}"
