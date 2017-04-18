#!/usr/bin/env python
##################################################
# Gnuradio Python Flow Graph
# Title: Top Block
# Generated: Mon Apr 17 16:06:36 2017
##################################################

from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from optparse import OptionParser
from threads import timer
import osmosdr
import time
import thread

class top_block(gr.top_block):

    def __init__(self):
        gr.top_block.__init__(self, "Top Block")

        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 3200000
        center_frequency = 262e6
        tLimit = 2
        ##################################################
        # Blocks
        ##################################################
        self.rtlsdr_source_1 = osmosdr.source( args="numchan=" + str(1) + " " + "rtl=1" )
        self.rtlsdr_source_1.set_sample_rate(samp_rate)
        self.rtlsdr_source_1.set_center_freq(100e6, 0)
        self.rtlsdr_source_1.set_freq_corr(0, 0)
        self.rtlsdr_source_1.set_dc_offset_mode(0, 0)
        self.rtlsdr_source_1.set_iq_balance_mode(0, 0)
        self.rtlsdr_source_1.set_gain_mode(False, 0)
        self.rtlsdr_source_1.set_gain(10, 0)
        self.rtlsdr_source_1.set_if_gain(20, 0)
        self.rtlsdr_source_1.set_bb_gain(20, 0)
        self.rtlsdr_source_1.set_antenna("", 0)
        self.rtlsdr_source_1.set_bandwidth(0, 0)
          
        self.rtlsdr_source_0 = osmosdr.source( args="numchan=" + str(1) + " " + "rtl=0" )
        self.rtlsdr_source_0.set_sample_rate(samp_rate)
        self.rtlsdr_source_0.set_center_freq(100e6, 0)
        self.rtlsdr_source_0.set_freq_corr(0, 0)
        self.rtlsdr_source_0.set_dc_offset_mode(0, 0)
        self.rtlsdr_source_0.set_iq_balance_mode(0, 0)
        self.rtlsdr_source_0.set_gain_mode(False, 0)
        self.rtlsdr_source_0.set_gain(10, 0)
        self.rtlsdr_source_0.set_if_gain(20, 0)  
        self.rtlsdr_source_0.set_bb_gain(20, 0)
        self.rtlsdr_source_0.set_antenna("", 0)
        self.rtlsdr_source_0.set_bandwidth(0, 0)
        t = time.asctime(time.localtime(time.time()))
        space = '_'
        fName = t[0]+t[1]+t[2]+space+t[4]+t[5]+t[6]+space+t[8]+t[9]+space+t[11]+t[12]+space+t[14]+t[15]+space+t[17]+t[18]+space+t[20]+t[21]+t[22]+t[23]
        fName = fName + space + "center_freq" + repr(center_frequency)+ space + "samp_rate" + repr(samp_rate) 
        f = open(fName, "wb+")       
        fName2 = fName + "_sdr2"
        f2 = open(fName2, "wb+")

        self.blocks_file_sink_1 = blocks.file_sink(gr.sizeof_gr_complex*1, fName, True)
        self.blocks_file_sink_1.set_unbuffered(False)
        self.blocks_file_sink_0 = blocks.file_sink(gr.sizeof_gr_complex*1, fName2, True)
        self.blocks_file_sink_0.set_unbuffered(False)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.rtlsdr_source_0, 0), (self.blocks_file_sink_1, 0))
        self.connect((self.rtlsdr_source_1, 0), (self.blocks_file_sink_0, 0))



    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.rtlsdr_source_1.set_sample_rate(self.samp_rate)
        self.rtlsdr_source_0.set_sample_rate(self.samp_rate)

if __name__ == '__main__':
    parser = OptionParser(option_class=eng_option, usage="%prog: [options]")
    (options, args) = parser.parse_args()
    tb = top_block()
    tb.start()
    threadTimer = timer(5)
    threadTimer.start()
