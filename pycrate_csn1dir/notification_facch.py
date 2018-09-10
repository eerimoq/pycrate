# -*- coding: UTF-8 -*-
#/**
# * Software Name : pycrate
# * Version : 0.3
# *
# * Copyright 2018. Benoit Michau. ANSSI.
# *
# * This library is free software; you can redistribute it and/or
# * modify it under the terms of the GNU Lesser General Public
# * License as published by the Free Software Foundation; either
# * version 2.1 of the License, or (at your option) any later version.
# *
# * This library is distributed in the hope that it will be useful,
# * but WITHOUT ANY WARRANTY; without even the implied warranty of
# * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# * Lesser General Public License for more details.
# *
# * You should have received a copy of the GNU Lesser General Public
# * License along with this library; if not, write to the Free Software
# * Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, 
# * MA 02110-1301  USA
# *
# *--------------------------------------------------------
# * File Name : pycrate_csn1dir/notification_facch.py
# * Created : 2018-07-30
# * Authors : Benoit Michau
# *--------------------------------------------------------
#*/
# specification: TS 44.018 - d80
# section: 9.1.21a Notification/FACCH
# top-level object: NOTIFICATION FACCH



# code automatically generated by pycrate_csn1
# change object type with type=CSN1T_BSTR (default type is CSN1T_UINT) in init
# add dict for value interpretation with dic={...} in CSN1Bit init
# add dict for key interpretation with kdic={...} in CSN1Alt init

from pycrate_csn1.csnobj import *

spare_padding = CSN1Val(name='spare_padding', val='L', num=-1)
Spare_padding = spare_padding
Spare_Padding = spare_padding 

nas_type4_lv = CSN1List(name='nas_type4_lv', list=[
  CSN1Bit(name='length', bit=8),
  CSN1Bit(name='value', bit=([0], lambda x: 8 * x))])

priority_uplink_access = CSN1Alt(name='priority_uplink_access', alt={
  'H': ('', []),
  'L': ('', [])})

group_channel_description = CSN1List(name='group_channel_description', list=[
  CSN1Bit(name='channel_description', bit=24),
  CSN1Alt(alt={
    '0': ('', []),
    '1': ('', [
    CSN1Alt(alt={
      '0': ('', [
      CSN1Ref(name='mobile_allocation', obj=nas_type4_lv)]),
      '1': ('', [
      CSN1Bit(name='frequency_short_list', bit=64)])})])})])

paging_information = CSN1List(name='paging_information', list=[
  CSN1Ref(name='mobile_identity', obj=nas_type4_lv),
  CSN1Bit(name='channel_first', bit=2),
  CSN1Alt(alt={
    '0': ('', []),
    '1': ('', [
    CSN1Bit(name='emlpp_priority', bit=3)])})])

emergency_ind = CSN1Alt(name='emergency_ind', alt={
  'H': ('', []),
  'L': ('', [])})

group_call_information = CSN1List(name='group_call_information', list=[
  CSN1Bit(name='group_call_reference', bit=36),
  CSN1Alt(alt={
    '0': ('', []),
    '1': ('', [
    CSN1Ref(obj=group_channel_description)])})])

notification_facch = CSN1List(name='notification_facch', list=[
  CSN1Bit(name='rr_short_pd'),
  CSN1Bit(name='message_type', bit=5),
  CSN1Bit(name='short_layer_2_header', bit=2),
  CSN1Alt(alt={
    '0': ('', [
    CSN1Ref(obj=group_call_information)]),
    '1': ('', [
    CSN1Ref(obj=paging_information)])}),
  CSN1Alt(alt={
    'H': ('', [
    CSN1Alt(alt={
      '0': ('', []),
      '1': ('', [
      CSN1Bit(name='cell_global_count', bit=2),
      CSN1Bit(name='b22_count')])}),
    CSN1Alt(alt={
      '0': ('', []),
      '1': ('', [
      CSN1Bit(name='vstk_rand', bit=36)])})]),
    'L': ('', []),
    None: ('', [])}),
  CSN1Alt(alt={
    'H': ('', [
    CSN1Bit(name='priority_uplink_access'),
    CSN1Bit(name='emergency_ind'),
    CSN1Alt(alt={
      '0': ('', []),
      '1': ('', [
      CSN1Bit(name='amr_config', bit=4)])}),
    CSN1Alt(alt={
      '0': ('', []),
      '1': ('', [
      CSN1Bit(name='paging_cause', bit=2)])}),
    CSN1Alt(alt={
      '0': ('', []),
      '1': ('', [
      CSN1Bit(name='sms_data_confidentiality_ind'),
      CSN1Bit(name='sms_guaranteed_privacy_ind')])})]),
    'L': ('', []),
    None: ('', [])}),
  CSN1Ref(obj=spare_padding)])
