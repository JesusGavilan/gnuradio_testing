#!/usr/bin/env python
##################################################
# Gnuradio Python Flow Graph
# Title: Tono llamada
# Generated: Mon Feb 24 12:07:59 2014
##################################################

from gnuradio import analog
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio import wxgui
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from gnuradio.wxgui import forms
from gnuradio.wxgui import scopesink2
from grc_gnuradio import wxgui as grc_wxgui
from optparse import OptionParser
import wx

class dial_tone(grc_wxgui.top_block_gui):

    def __init__(self):
        grc_wxgui.top_block_gui.__init__(self, title="Tono llamada")
        _icon_path = "/usr/share/icons/hicolor/32x32/apps/gnuradio-grc.png"
        self.SetIcon(wx.Icon(_icon_path, wx.BITMAP_TYPE_ANY))

        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 32000
        self.f2 = f2 = 350
        self.f1 = f1 = 350
        self.A2 = A2 = 0.100
        self.A1 = A1 = 0.100

        ##################################################
        # Blocks
        ##################################################
        _f2_sizer = wx.BoxSizer(wx.VERTICAL)
        self._f2_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_f2_sizer,
        	value=self.f2,
        	callback=self.set_f2,
        	label="Frecuencia tono 1Hz",
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._f2_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_f2_sizer,
        	value=self.f2,
        	callback=self.set_f2,
        	minimum=0,
        	maximum=1000,
        	num_steps=100,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.GridAdd(_f2_sizer, 3, 0, 1, 2)
        _f1_sizer = wx.BoxSizer(wx.VERTICAL)
        self._f1_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_f1_sizer,
        	value=self.f1,
        	callback=self.set_f1,
        	label="Frecuencia tono 1Hz",
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._f1_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_f1_sizer,
        	value=self.f1,
        	callback=self.set_f1,
        	minimum=0,
        	maximum=1000,
        	num_steps=100,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.GridAdd(_f1_sizer, 0, 0, 1, 2)
        _A2_sizer = wx.BoxSizer(wx.VERTICAL)
        self._A2_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_A2_sizer,
        	value=self.A2,
        	callback=self.set_A2,
        	label="Amplitud tono 1",
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._A2_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_A2_sizer,
        	value=self.A2,
        	callback=self.set_A2,
        	minimum=0,
        	maximum=1,
        	num_steps=1,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.GridAdd(_A2_sizer, 4, 0, 1, 2)
        _A1_sizer = wx.BoxSizer(wx.VERTICAL)
        self._A1_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_A1_sizer,
        	value=self.A1,
        	callback=self.set_A1,
        	label="Amplitud tono 1",
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._A1_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_A1_sizer,
        	value=self.A1,
        	callback=self.set_A1,
        	minimum=0,
        	maximum=1,
        	num_steps=1,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.GridAdd(_A1_sizer, 1, 0, 1, 2)
        self.wxgui_scopesink2_0 = scopesink2.scope_sink_c(
        	self.GetWin(),
        	title="Forma de onda",
        	sample_rate=samp_rate,
        	v_scale=0,
        	v_offset=0,
        	t_scale=0,
        	ac_couple=False,
        	xy_mode=False,
        	num_inputs=1,
        	trig_mode=wxgui.TRIG_MODE_AUTO,
        	y_axis_label="Counts",
        )
        self.Add(self.wxgui_scopesink2_0.win)
        self.blocks_add_xx_0 = blocks.add_vcc(1)
        self.analog_sig_source_x_0_0 = analog.sig_source_c(samp_rate, analog.GR_COS_WAVE, f2, A2, 0)
        self.analog_sig_source_x_0 = analog.sig_source_c(samp_rate, analog.GR_COS_WAVE, f1, A1, 0)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_sig_source_x_0, 0), (self.blocks_add_xx_0, 0))
        self.connect((self.analog_sig_source_x_0_0, 0), (self.blocks_add_xx_0, 1))
        self.connect((self.blocks_add_xx_0, 0), (self.wxgui_scopesink2_0, 0))


# QT sink close method reimplementation

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.analog_sig_source_x_0.set_sampling_freq(self.samp_rate)
        self.analog_sig_source_x_0_0.set_sampling_freq(self.samp_rate)
        self.wxgui_scopesink2_0.set_sample_rate(self.samp_rate)

    def get_f2(self):
        return self.f2

    def set_f2(self, f2):
        self.f2 = f2
        self._f2_slider.set_value(self.f2)
        self._f2_text_box.set_value(self.f2)
        self.analog_sig_source_x_0_0.set_frequency(self.f2)

    def get_f1(self):
        return self.f1

    def set_f1(self, f1):
        self.f1 = f1
        self._f1_slider.set_value(self.f1)
        self._f1_text_box.set_value(self.f1)
        self.analog_sig_source_x_0.set_frequency(self.f1)

    def get_A2(self):
        return self.A2

    def set_A2(self, A2):
        self.A2 = A2
        self._A2_slider.set_value(self.A2)
        self._A2_text_box.set_value(self.A2)
        self.analog_sig_source_x_0_0.set_amplitude(self.A2)

    def get_A1(self):
        return self.A1

    def set_A1(self, A1):
        self.A1 = A1
        self._A1_slider.set_value(self.A1)
        self._A1_text_box.set_value(self.A1)
        self.analog_sig_source_x_0.set_amplitude(self.A1)

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print "Warning: failed to XInitThreads()"
    parser = OptionParser(option_class=eng_option, usage="%prog: [options]")
    (options, args) = parser.parse_args()
    tb = dial_tone()
    tb.Start(True)
    tb.Wait()

