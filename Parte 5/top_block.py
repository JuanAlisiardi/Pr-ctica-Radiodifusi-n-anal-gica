#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: Top Block
# GNU Radio version: 3.10.5.1

from packaging.version import Version as StrictVersion

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print("Warning: failed to XInitThreads()")

from PyQt5 import Qt
from gnuradio import qtgui
from gnuradio.filter import firdes
import sip
from gnuradio import analog
import math
from gnuradio import blocks
from gnuradio import filter
from gnuradio import gr
from gnuradio.fft import window
import sys
import signal
from argparse import ArgumentParser
from gnuradio.eng_arg import eng_float, intx
from gnuradio import eng_notation
from gnuradio.qtgui import Range, RangeWidget
from PyQt5 import QtCore
import numpy as np



from gnuradio import qtgui

class top_block(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Top Block", catch_exceptions=True)
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Top Block")
        qtgui.util.check_set_qss()
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except:
            pass
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "top_block")

        try:
            if StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
                self.restoreGeometry(self.settings.value("geometry").toByteArray())
            else:
                self.restoreGeometry(self.settings.value("geometry"))
        except:
            pass

        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 2e6
        self.variable_low_pass_filter_taps_0 = variable_low_pass_filter_taps_0 = firdes.low_pass(1.0, samp_rate, 15e3,2e3, window.WIN_HAMMING, 6.76)
        self.gain = gain = 1
        self.frec_R = frec_R = 50
        self.frec_L = frec_L = 50
        self.fcia = fcia = 19e3
        self.deltaf = deltaf = 75e3
        self.amp_pilot = amp_pilot = 0.22
        self.Amplitud_LR = Amplitud_LR = 1

        ##################################################
        # Blocks
        ##################################################

        self._frec_R_range = Range(0, 15e3, 1, 50, 200)
        self._frec_R_win = RangeWidget(self._frec_R_range, self.set_frec_R, "'frec_R'", "counter_slider", float, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._frec_R_win)
        self._frec_L_range = Range(0, 15e3, 1, 50, 200)
        self._frec_L_win = RangeWidget(self._frec_L_range, self.set_frec_L, "'frec_L'", "counter_slider", float, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._frec_L_win)
        self._amp_pilot_range = Range(0, 1, 0.01, 0.22, 200)
        self._amp_pilot_win = RangeWidget(self._amp_pilot_range, self.set_amp_pilot, "'amp_pilot'", "counter_slider", float, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._amp_pilot_win)
        self._Amplitud_LR_range = Range(0, 1, 0.1, 1, 200)
        self._Amplitud_LR_win = RangeWidget(self._Amplitud_LR_range, self.set_Amplitud_LR, "'Amplitud_LR'", "counter_slider", float, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._Amplitud_LR_win)
        self.qtgui_freq_sink_x_1_0 = qtgui.freq_sink_f(
            1024, #size
            window.WIN_BLACKMAN_hARRIS, #wintype
            0, #fc
            samp_rate, #bw
            "", #name
            1,
            None # parent
        )
        self.qtgui_freq_sink_x_1_0.set_update_time(0.10)
        self.qtgui_freq_sink_x_1_0.set_y_axis((-140), 10)
        self.qtgui_freq_sink_x_1_0.set_y_label('Relative Gain', 'dB')
        self.qtgui_freq_sink_x_1_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_1_0.enable_autoscale(False)
        self.qtgui_freq_sink_x_1_0.enable_grid(False)
        self.qtgui_freq_sink_x_1_0.set_fft_average(1.0)
        self.qtgui_freq_sink_x_1_0.enable_axis_labels(True)
        self.qtgui_freq_sink_x_1_0.enable_control_panel(False)
        self.qtgui_freq_sink_x_1_0.set_fft_window_normalized(False)


        self.qtgui_freq_sink_x_1_0.set_plot_pos_half(not False)

        labels = ['', '', '', '', '',
            '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
            "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]

        for i in range(1):
            if len(labels[i]) == 0:
                self.qtgui_freq_sink_x_1_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_1_0.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_1_0.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_1_0.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_1_0.set_line_alpha(i, alphas[i])

        self._qtgui_freq_sink_x_1_0_win = sip.wrapinstance(self.qtgui_freq_sink_x_1_0.qwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_freq_sink_x_1_0_win)
        self.qtgui_freq_sink_x_0 = qtgui.freq_sink_f(
            8192, #size
            window.WIN_BLACKMAN_hARRIS, #wintype
            0, #fc
            samp_rate, #bw
            "", #name
            1,
            None # parent
        )
        self.qtgui_freq_sink_x_0.set_update_time(0.10)
        self.qtgui_freq_sink_x_0.set_y_axis((-140), 10)
        self.qtgui_freq_sink_x_0.set_y_label('Relative Gain', 'dB')
        self.qtgui_freq_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_0.enable_autoscale(False)
        self.qtgui_freq_sink_x_0.enable_grid(False)
        self.qtgui_freq_sink_x_0.set_fft_average(1.0)
        self.qtgui_freq_sink_x_0.enable_axis_labels(True)
        self.qtgui_freq_sink_x_0.enable_control_panel(False)
        self.qtgui_freq_sink_x_0.set_fft_window_normalized(False)


        self.qtgui_freq_sink_x_0.set_plot_pos_half(not False)

        labels = ['', '', '', '', '',
            '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
            "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]

        for i in range(1):
            if len(labels[i]) == 0:
                self.qtgui_freq_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_0.set_line_alpha(i, alphas[i])

        self._qtgui_freq_sink_x_0_win = sip.wrapinstance(self.qtgui_freq_sink_x_0.qwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_freq_sink_x_0_win)
        self.low_pass_filter_0_0 = filter.fir_filter_fff(
            1,
            firdes.low_pass(
                1,
                samp_rate,
                15e3,
                1e3,
                window.WIN_HAMMING,
                6.76))
        self.low_pass_filter_0 = filter.fir_filter_fff(
            1,
            firdes.low_pass(
                1,
                samp_rate,
                15e3,
                1e3,
                window.WIN_HAMMING,
                6.76))
        self._gain_range = Range(0, 40, 1, 1, 200)
        self._gain_win = RangeWidget(self._gain_range, self.set_gain, "'gain'", "counter_slider", float, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._gain_win)
        self.fir_filter_xxx_0_0 = filter.fir_filter_fff(10, variable_low_pass_filter_taps_0)
        self.fir_filter_xxx_0_0.declare_sample_delay(0)
        self.fir_filter_xxx_0 = filter.fir_filter_fff(10, variable_low_pass_filter_taps_0)
        self.fir_filter_xxx_0.declare_sample_delay(0)
        self._fcia_range = Range(18e3, 20e3, 100, 19e3, 200)
        self._fcia_win = RangeWidget(self._fcia_range, self.set_fcia, "fcia", "counter_slider", float, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._fcia_win)
        self.blocks_throttle_0 = blocks.throttle(gr.sizeof_float*1, samp_rate,True)
        self.blocks_sub_xx_0_0 = blocks.sub_ff(1)
        self.blocks_sub_xx_0 = blocks.sub_ff(1)
        self.blocks_multiply_xx_1 = blocks.multiply_vff(1)
        self.blocks_multiply_xx_0_0 = blocks.multiply_vff(1)
        self.blocks_multiply_xx_0 = blocks.multiply_vcc(1)
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_ff(2)
        self.blocks_float_to_complex_0 = blocks.float_to_complex(1)
        self.blocks_complex_to_imag_0 = blocks.complex_to_imag(1)
        self.blocks_add_xx_1 = blocks.add_vff(1)
        self.blocks_add_xx_0_0 = blocks.add_vff(1)
        self.blocks_add_xx_0 = blocks.add_vff(1)
        self.analog_sig_source_x_3 = analog.sig_source_f(samp_rate, analog.GR_COS_WAVE, frec_R, Amplitud_LR, 0, 0)
        self.analog_sig_source_x_2 = analog.sig_source_f(samp_rate, analog.GR_COS_WAVE, frec_L, Amplitud_LR, 0, 0)
        self.analog_sig_source_x_1 = analog.sig_source_f(samp_rate, analog.GR_SIN_WAVE, 38e3, 1, 0, 0)
        self.analog_sig_source_x_0 = analog.sig_source_f(samp_rate, analog.GR_SIN_WAVE, 19e3, amp_pilot, 0, 0)
        self.analog_quadrature_demod_cf_0 = analog.quadrature_demod_cf((samp_rate/(2*np.pi*deltaf)))
        self.analog_pll_refout_cc_0 = analog.pll_refout_cc((100e-6), (2 *np.pi* 19200 / samp_rate), (2 * np.pi* 18800 / samp_rate))
        self.analog_frequency_modulator_fc_0 = analog.frequency_modulator_fc((2*np.pi*deltaf/samp_rate))
        self.analog_const_source_x_0 = analog.sig_source_f(0, analog.GR_CONST_WAVE, 0, 0, 0)


        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_const_source_x_0, 0), (self.blocks_float_to_complex_0, 1))
        self.connect((self.analog_frequency_modulator_fc_0, 0), (self.analog_quadrature_demod_cf_0, 0))
        self.connect((self.analog_pll_refout_cc_0, 0), (self.blocks_multiply_xx_0, 1))
        self.connect((self.analog_pll_refout_cc_0, 0), (self.blocks_multiply_xx_0, 0))
        self.connect((self.analog_quadrature_demod_cf_0, 0), (self.blocks_float_to_complex_0, 0))
        self.connect((self.analog_quadrature_demod_cf_0, 0), (self.blocks_multiply_xx_1, 0))
        self.connect((self.analog_quadrature_demod_cf_0, 0), (self.low_pass_filter_0_0, 0))
        self.connect((self.analog_sig_source_x_0, 0), (self.blocks_add_xx_1, 0))
        self.connect((self.analog_sig_source_x_1, 0), (self.blocks_multiply_xx_0_0, 0))
        self.connect((self.analog_sig_source_x_2, 0), (self.blocks_add_xx_0_0, 0))
        self.connect((self.analog_sig_source_x_2, 0), (self.blocks_sub_xx_0, 0))
        self.connect((self.analog_sig_source_x_3, 0), (self.blocks_add_xx_0_0, 1))
        self.connect((self.analog_sig_source_x_3, 0), (self.blocks_sub_xx_0, 1))
        self.connect((self.blocks_add_xx_0, 0), (self.fir_filter_xxx_0, 0))
        self.connect((self.blocks_add_xx_0_0, 0), (self.blocks_add_xx_1, 2))
        self.connect((self.blocks_add_xx_1, 0), (self.blocks_throttle_0, 0))
        self.connect((self.blocks_complex_to_imag_0, 0), (self.blocks_multiply_xx_1, 1))
        self.connect((self.blocks_float_to_complex_0, 0), (self.analog_pll_refout_cc_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.low_pass_filter_0, 0))
        self.connect((self.blocks_multiply_xx_0, 0), (self.blocks_complex_to_imag_0, 0))
        self.connect((self.blocks_multiply_xx_0_0, 0), (self.blocks_add_xx_1, 1))
        self.connect((self.blocks_multiply_xx_1, 0), (self.blocks_multiply_const_vxx_0, 0))
        self.connect((self.blocks_sub_xx_0, 0), (self.blocks_multiply_xx_0_0, 1))
        self.connect((self.blocks_sub_xx_0_0, 0), (self.fir_filter_xxx_0_0, 0))
        self.connect((self.blocks_throttle_0, 0), (self.analog_frequency_modulator_fc_0, 0))
        self.connect((self.fir_filter_xxx_0, 0), (self.qtgui_freq_sink_x_0, 0))
        self.connect((self.fir_filter_xxx_0_0, 0), (self.qtgui_freq_sink_x_1_0, 0))
        self.connect((self.low_pass_filter_0, 0), (self.blocks_add_xx_0, 1))
        self.connect((self.low_pass_filter_0, 0), (self.blocks_sub_xx_0_0, 1))
        self.connect((self.low_pass_filter_0_0, 0), (self.blocks_add_xx_0, 0))
        self.connect((self.low_pass_filter_0_0, 0), (self.blocks_sub_xx_0_0, 0))


    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "top_block")
        self.settings.setValue("geometry", self.saveGeometry())
        self.stop()
        self.wait()

        event.accept()

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.set_variable_low_pass_filter_taps_0(firdes.low_pass(1.0, self.samp_rate, 15e3, 2e3, window.WIN_HAMMING, 6.76))
        self.analog_frequency_modulator_fc_0.set_sensitivity((2*np.pi*self.deltaf/self.samp_rate))
        self.analog_pll_refout_cc_0.set_max_freq((2 *np.pi* 19200 / self.samp_rate))
        self.analog_pll_refout_cc_0.set_min_freq((2 * np.pi* 18800 / self.samp_rate))
        self.analog_quadrature_demod_cf_0.set_gain((self.samp_rate/(2*np.pi*self.deltaf)))
        self.analog_sig_source_x_0.set_sampling_freq(self.samp_rate)
        self.analog_sig_source_x_1.set_sampling_freq(self.samp_rate)
        self.analog_sig_source_x_2.set_sampling_freq(self.samp_rate)
        self.analog_sig_source_x_3.set_sampling_freq(self.samp_rate)
        self.blocks_throttle_0.set_sample_rate(self.samp_rate)
        self.low_pass_filter_0.set_taps(firdes.low_pass(1, self.samp_rate, 15e3, 1e3, window.WIN_HAMMING, 6.76))
        self.low_pass_filter_0_0.set_taps(firdes.low_pass(1, self.samp_rate, 15e3, 1e3, window.WIN_HAMMING, 6.76))
        self.qtgui_freq_sink_x_0.set_frequency_range(0, self.samp_rate)
        self.qtgui_freq_sink_x_1_0.set_frequency_range(0, self.samp_rate)

    def get_variable_low_pass_filter_taps_0(self):
        return self.variable_low_pass_filter_taps_0

    def set_variable_low_pass_filter_taps_0(self, variable_low_pass_filter_taps_0):
        self.variable_low_pass_filter_taps_0 = variable_low_pass_filter_taps_0
        self.fir_filter_xxx_0.set_taps(self.variable_low_pass_filter_taps_0)
        self.fir_filter_xxx_0_0.set_taps(self.variable_low_pass_filter_taps_0)

    def get_gain(self):
        return self.gain

    def set_gain(self, gain):
        self.gain = gain

    def get_frec_R(self):
        return self.frec_R

    def set_frec_R(self, frec_R):
        self.frec_R = frec_R
        self.analog_sig_source_x_3.set_frequency(self.frec_R)

    def get_frec_L(self):
        return self.frec_L

    def set_frec_L(self, frec_L):
        self.frec_L = frec_L
        self.analog_sig_source_x_2.set_frequency(self.frec_L)

    def get_fcia(self):
        return self.fcia

    def set_fcia(self, fcia):
        self.fcia = fcia

    def get_deltaf(self):
        return self.deltaf

    def set_deltaf(self, deltaf):
        self.deltaf = deltaf
        self.analog_frequency_modulator_fc_0.set_sensitivity((2*np.pi*self.deltaf/self.samp_rate))
        self.analog_quadrature_demod_cf_0.set_gain((self.samp_rate/(2*np.pi*self.deltaf)))

    def get_amp_pilot(self):
        return self.amp_pilot

    def set_amp_pilot(self, amp_pilot):
        self.amp_pilot = amp_pilot
        self.analog_sig_source_x_0.set_amplitude(self.amp_pilot)

    def get_Amplitud_LR(self):
        return self.Amplitud_LR

    def set_Amplitud_LR(self, Amplitud_LR):
        self.Amplitud_LR = Amplitud_LR
        self.analog_sig_source_x_2.set_amplitude(self.Amplitud_LR)
        self.analog_sig_source_x_3.set_amplitude(self.Amplitud_LR)




def main(top_block_cls=top_block, options=None):

    if StrictVersion("4.5.0") <= StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()

    tb.start()

    tb.show()

    def sig_handler(sig=None, frame=None):
        tb.stop()
        tb.wait()

        Qt.QApplication.quit()

    signal.signal(signal.SIGINT, sig_handler)
    signal.signal(signal.SIGTERM, sig_handler)

    timer = Qt.QTimer()
    timer.start(500)
    timer.timeout.connect(lambda: None)

    qapp.exec_()

if __name__ == '__main__':
    main()
