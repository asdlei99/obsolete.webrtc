# Copyright (c) 2011 The WebRTC project authors. All Rights Reserved.
#
# Use of this source code is governed by a BSD-style license
# that can be found in the LICENSE file in the root of the source
# tree. An additional intellectual property rights grant can be found
# in the file PATENTS.  All contributing project authors may
# be found in the AUTHORS file in the root of the source tree.

{
  'includes': [
    '../build/common.gypi',
    'audio_coding/audio_coding.gypi',
    'audio_conference_mixer/audio_conference_mixer.gypi',
    'audio_device/audio_device.gypi',
    'audio_processing/audio_processing.gypi',
    'bitrate_controller/bitrate_controller.gypi',
    'desktop_capture/desktop_capture.gypi',
    'media_file/media_file.gypi',
    'pacing/pacing.gypi',
    'remote_bitrate_estimator/remote_bitrate_estimator.gypi',
    'rtp_rtcp/rtp_rtcp.gypi',
    'utility/utility.gypi',
    'video_coding/codecs/h264/h264.gypi',
    'video_coding/codecs/i420/main/source/i420.gypi',
    'video_coding/video_coding.gypi',
    'video_capture/video_capture.gypi',
    'video_processing/video_processing.gypi',
    'video_render/video_render.gypi',
  ],
  'conditions': [
    ['include_tests==1', {
      'includes': [
        'audio_coding/audio_coding_tests.gypi',
        'audio_processing/audio_processing_tests.gypi',
        'rtp_rtcp/test/testFec/test_fec.gypi',
        'video_coding/video_coding_test.gypi',
        'video_coding/codecs/test/video_codecs_test_framework.gypi',
        'video_coding/codecs/tools/video_codecs_tools.gypi',
      ], # includes
      'variables': {
        'conditions': [
          # Desktop capturer is supported only on Windows, OSX and Linux.
          ['OS=="win" or OS=="mac" or OS=="linux"', {
            'desktop_capture_supported%': 1,
          }, {
            'desktop_capture_supported%': 0,
          }],
        ],
      },
      'targets': [
        {
          'target_name': 'modules_unittests',
          'type': '<(gtest_target_type)',
          'defines': [
            '<@(audio_coding_defines)',
          ],
          'dependencies': [
            'acm_receive_test',
            'acm_send_test',
            'audio_coding_module',
            'audio_conference_mixer',
            'audio_device'  ,
            'audio_processing',
            'audioproc_test_utils',
            'bitrate_controller',
            'bwe_simulator',
            'cng',
            'desktop_capture',
            'isac_fix',
            'media_file',
            'neteq',
            'neteq_test_support',
            'neteq_unittest_tools',
            'paced_sender',
            'pcm16b',  # Needed by NetEq tests.
            'red',
            'remote_bitrate_estimator',
            'rtp_rtcp',
            'video_codecs_test_framework',
            'video_processing',
            'webrtc_utility',
            'webrtc_video_coding',
            '<@(neteq_dependencies)',
            '<(DEPTH)/testing/gmock.gyp:gmock',
            '<(DEPTH)/testing/gtest.gyp:gtest',
            '<(DEPTH)/third_party/gflags/gflags.gyp:gflags',
            '<(webrtc_root)/common.gyp:webrtc_common',
            '<(webrtc_root)/common_audio/common_audio.gyp:common_audio',
            '<(webrtc_root)/modules/modules.gyp:video_capture',
            '<(webrtc_root)/modules/video_coding/codecs/vp8/vp8.gyp:webrtc_vp8',
            '<(webrtc_root)/modules/video_coding/codecs/vp9/vp9.gyp:webrtc_vp9',
            '<(webrtc_root)/system_wrappers/system_wrappers.gyp:system_wrappers',
            '<(webrtc_root)/test/test.gyp:frame_generator',
            '<(webrtc_root)/test/test.gyp:rtp_test_utils',
            '<(webrtc_root)/test/test.gyp:test_support_main',
            '<(webrtc_root)/tools/tools.gyp:agc_test_utils',
          ],
          'sources': [
            'audio_coding/codecs/cng/audio_encoder_cng_unittest.cc',
            'audio_coding/main/acm2/acm_receiver_unittest.cc',
            'audio_coding/main/acm2/acm_receiver_unittest_oldapi.cc',
            'audio_coding/main/acm2/audio_coding_module_unittest.cc',
            'audio_coding/main/acm2/audio_coding_module_unittest_oldapi.cc',
            'audio_coding/main/acm2/call_statistics_unittest.cc',
            'audio_coding/main/acm2/codec_owner_unittest.cc',
            'audio_coding/main/acm2/initial_delay_manager_unittest.cc',
            'audio_coding/main/acm2/nack_unittest.cc',
            'audio_coding/codecs/cng/cng_unittest.cc',
            'audio_coding/codecs/isac/fix/source/filters_unittest.cc',
            'audio_coding/codecs/isac/fix/source/filterbanks_unittest.cc',
            'audio_coding/codecs/isac/fix/source/lpc_masking_model_unittest.cc',
            'audio_coding/codecs/isac/fix/source/transform_unittest.cc',
            'audio_coding/codecs/isac/main/source/audio_encoder_isac_unittest.cc',
            'audio_coding/codecs/isac/main/source/isac_unittest.cc',
            'audio_coding/codecs/isac/unittest.cc',
            'audio_coding/codecs/opus/audio_encoder_opus_unittest.cc',
            'audio_coding/codecs/opus/opus_unittest.cc',
            'audio_coding/codecs/red/audio_encoder_copy_red_unittest.cc',
            'audio_coding/neteq/audio_classifier_unittest.cc',
            'audio_coding/neteq/audio_multi_vector_unittest.cc',
            'audio_coding/neteq/audio_vector_unittest.cc',
            'audio_coding/neteq/background_noise_unittest.cc',
            'audio_coding/neteq/buffer_level_filter_unittest.cc',
            'audio_coding/neteq/comfort_noise_unittest.cc',
            'audio_coding/neteq/decision_logic_unittest.cc',
            'audio_coding/neteq/decoder_database_unittest.cc',
            'audio_coding/neteq/delay_manager_unittest.cc',
            'audio_coding/neteq/delay_peak_detector_unittest.cc',
            'audio_coding/neteq/dsp_helper_unittest.cc',
            'audio_coding/neteq/dtmf_buffer_unittest.cc',
            'audio_coding/neteq/dtmf_tone_generator_unittest.cc',
            'audio_coding/neteq/expand_unittest.cc',
            'audio_coding/neteq/merge_unittest.cc',
            'audio_coding/neteq/neteq_external_decoder_unittest.cc',
            'audio_coding/neteq/neteq_impl_unittest.cc',
            'audio_coding/neteq/neteq_network_stats_unittest.cc',
            'audio_coding/neteq/neteq_stereo_unittest.cc',
            'audio_coding/neteq/neteq_unittest.cc',
            'audio_coding/neteq/normal_unittest.cc',
            'audio_coding/neteq/packet_buffer_unittest.cc',
            'audio_coding/neteq/payload_splitter_unittest.cc',
            'audio_coding/neteq/post_decode_vad_unittest.cc',
            'audio_coding/neteq/random_vector_unittest.cc',
            'audio_coding/neteq/sync_buffer_unittest.cc',
            'audio_coding/neteq/timestamp_scaler_unittest.cc',
            'audio_coding/neteq/time_stretch_unittest.cc',
            'audio_coding/neteq/mock/mock_audio_decoder.h',
            'audio_coding/neteq/mock/mock_audio_vector.h',
            'audio_coding/neteq/mock/mock_buffer_level_filter.h',
            'audio_coding/neteq/mock/mock_decoder_database.h',
            'audio_coding/neteq/mock/mock_delay_manager.h',
            'audio_coding/neteq/mock/mock_delay_peak_detector.h',
            'audio_coding/neteq/mock/mock_dtmf_buffer.h',
            'audio_coding/neteq/mock/mock_dtmf_tone_generator.h',
            'audio_coding/neteq/mock/mock_expand.h',
            'audio_coding/neteq/mock/mock_external_decoder_pcm16b.h',
            'audio_coding/neteq/mock/mock_packet_buffer.h',
            'audio_coding/neteq/mock/mock_payload_splitter.h',
            'audio_coding/neteq/tools/input_audio_file_unittest.cc',
            'audio_coding/neteq/tools/packet_unittest.cc',
            'audio_conference_mixer/test/audio_conference_mixer_unittest.cc',
            'audio_device/fine_audio_buffer_unittest.cc',
            'audio_processing/aec/echo_cancellation_unittest.cc',
            'audio_processing/aec/system_delay_unittest.cc',
            # TODO(ajm): Fix to match new interface.
            # 'audio_processing/agc/agc_unittest.cc',
            'audio_processing/agc/histogram_unittest.cc',
            'audio_processing/agc/mock_agc.h',
            'audio_processing/beamformer/complex_matrix_unittest.cc',
            'audio_processing/beamformer/covariance_matrix_generator_unittest.cc',
            'audio_processing/beamformer/matrix_unittest.cc',
            'audio_processing/beamformer/mock_nonlinear_beamformer.h',
            'audio_processing/echo_cancellation_impl_unittest.cc',
            'audio_processing/intelligibility/intelligibility_enhancer_unittest.cc',
            'audio_processing/intelligibility/intelligibility_utils_unittest.cc',
            'audio_processing/splitting_filter_unittest.cc',
            'audio_processing/transient/dyadic_decimator_unittest.cc',
            'audio_processing/transient/file_utils.cc',
            'audio_processing/transient/file_utils.h',
            'audio_processing/transient/file_utils_unittest.cc',
            'audio_processing/transient/moving_moments_unittest.cc',
            'audio_processing/transient/transient_detector_unittest.cc',
            'audio_processing/transient/transient_suppressor_unittest.cc',
            'audio_processing/transient/wpd_node_unittest.cc',
            'audio_processing/transient/wpd_tree_unittest.cc',
            'audio_processing/utility/delay_estimator_unittest.cc',
            'audio_processing/vad/gmm_unittest.cc',
            'audio_processing/vad/pitch_based_vad_unittest.cc',
            'audio_processing/vad/pitch_internal_unittest.cc',
            'audio_processing/vad/pole_zero_filter_unittest.cc',
            'audio_processing/vad/standalone_vad_unittest.cc',
            'audio_processing/vad/vad_audio_proc_unittest.cc',
            'audio_processing/vad/vad_circular_buffer_unittest.cc',
            'audio_processing/vad/voice_activity_detector_unittest.cc',
            'bitrate_controller/bitrate_allocator_unittest.cc',
            'bitrate_controller/bitrate_controller_unittest.cc',
            'bitrate_controller/send_side_bandwidth_estimation_unittest.cc',
            'desktop_capture/desktop_and_cursor_composer_unittest.cc',
            'desktop_capture/desktop_region_unittest.cc',
            'desktop_capture/differ_block_unittest.cc',
            'desktop_capture/differ_unittest.cc',
            'desktop_capture/mouse_cursor_monitor_unittest.cc',
            'desktop_capture/screen_capturer_helper_unittest.cc',
            'desktop_capture/screen_capturer_mac_unittest.cc',
            'desktop_capture/screen_capturer_mock_objects.h',
            'desktop_capture/screen_capturer_unittest.cc',
            'desktop_capture/window_capturer_unittest.cc',
            'desktop_capture/win/cursor_unittest.cc',
            'desktop_capture/win/cursor_unittest_resources.h',
            'desktop_capture/win/cursor_unittest_resources.rc',
            'media_file/source/media_file_unittest.cc',
            'module_common_types_unittest.cc',
            'pacing/bitrate_prober_unittest.cc',
            'pacing/paced_sender_unittest.cc',
            'pacing/packet_router_unittest.cc',
            'remote_bitrate_estimator/bwe_simulations.cc',
            'remote_bitrate_estimator/include/mock/mock_remote_bitrate_observer.h',
            'remote_bitrate_estimator/inter_arrival_unittest.cc',
            'remote_bitrate_estimator/overuse_detector_unittest.cc',
            'remote_bitrate_estimator/rate_statistics_unittest.cc',
            'remote_bitrate_estimator/remote_bitrate_estimator_abs_send_time_unittest.cc',
            'remote_bitrate_estimator/remote_bitrate_estimator_single_stream_unittest.cc',
            'remote_bitrate_estimator/remote_bitrate_estimator_unittest_helper.cc',
            'remote_bitrate_estimator/remote_bitrate_estimator_unittest_helper.h',
            'remote_bitrate_estimator/remote_estimator_proxy_unittest.cc',
            'remote_bitrate_estimator/send_time_history_unittest.cc',
            'remote_bitrate_estimator/test/bwe_test_framework_unittest.cc',
            'remote_bitrate_estimator/test/bwe_unittest.cc',
            'remote_bitrate_estimator/test/metric_recorder_unittest.cc',
            'remote_bitrate_estimator/test/estimators/nada_unittest.cc',
            'remote_bitrate_estimator/transport_feedback_adapter_unittest.cc',
            'rtp_rtcp/source/mock/mock_rtp_payload_strategy.h',
            'rtp_rtcp/source/byte_io_unittest.cc',
            'rtp_rtcp/source/fec_receiver_unittest.cc',
            'rtp_rtcp/source/fec_test_helper.cc',
            'rtp_rtcp/source/fec_test_helper.h',
            'rtp_rtcp/source/h264_sps_parser_unittest.cc',
            'rtp_rtcp/source/nack_rtx_unittest.cc',
            'rtp_rtcp/source/packet_loss_stats_unittest.cc',
            'rtp_rtcp/source/producer_fec_unittest.cc',
            'rtp_rtcp/source/receive_statistics_unittest.cc',
            'rtp_rtcp/source/remote_ntp_time_estimator_unittest.cc',
            'rtp_rtcp/source/rtcp_format_remb_unittest.cc',
            'rtp_rtcp/source/rtcp_packet_unittest.cc',
            'rtp_rtcp/source/rtcp_packet/transport_feedback_unittest.cc',
            'rtp_rtcp/source/rtcp_receiver_unittest.cc',
            'rtp_rtcp/source/rtcp_sender_unittest.cc',
            'rtp_rtcp/source/rtcp_utility_unittest.cc',
            'rtp_rtcp/source/rtp_fec_unittest.cc',
            'rtp_rtcp/source/rtp_format_h264_unittest.cc',
            'rtp_rtcp/source/rtp_format_vp8_test_helper.cc',
            'rtp_rtcp/source/rtp_format_vp8_test_helper.h',
            'rtp_rtcp/source/rtp_format_vp8_unittest.cc',
            'rtp_rtcp/source/rtp_format_vp9_unittest.cc',
            'rtp_rtcp/source/rtp_packet_history_unittest.cc',
            'rtp_rtcp/source/rtp_payload_registry_unittest.cc',
            'rtp_rtcp/source/rtp_rtcp_impl_unittest.cc',
            'rtp_rtcp/source/rtp_header_extension_unittest.cc',
            'rtp_rtcp/source/rtp_sender_unittest.cc',
            'rtp_rtcp/source/vp8_partition_aggregator_unittest.cc',
            'rtp_rtcp/test/testAPI/test_api.cc',
            'rtp_rtcp/test/testAPI/test_api.h',
            'rtp_rtcp/test/testAPI/test_api_audio.cc',
            'rtp_rtcp/test/testAPI/test_api_rtcp.cc',
            'rtp_rtcp/test/testAPI/test_api_video.cc',
            'utility/source/audio_frame_operations_unittest.cc',
            'utility/source/file_player_unittests.cc',
            'utility/source/process_thread_impl_unittest.cc',
            'video_coding/codecs/test/packet_manipulator_unittest.cc',
            'video_coding/codecs/test/stats_unittest.cc',
            'video_coding/codecs/test/videoprocessor_unittest.cc',
            'video_coding/codecs/vp8/default_temporal_layers_unittest.cc',
            'video_coding/codecs/vp8/reference_picture_selection_unittest.cc',
            'video_coding/codecs/vp8/screenshare_layers_unittest.cc',
            'video_coding/codecs/vp8/simulcast_encoder_adapter_unittest.cc',
            'video_coding/codecs/vp8/simulcast_unittest.cc',
            'video_coding/codecs/vp8/simulcast_unittest.h',
            'video_coding/main/interface/mock/mock_vcm_callbacks.h',
            'video_coding/main/source/decoding_state_unittest.cc',
            'video_coding/main/source/jitter_buffer_unittest.cc',
            'video_coding/main/source/jitter_estimator_tests.cc',
            'video_coding/main/source/media_optimization_unittest.cc',
            'video_coding/main/source/receiver_unittest.cc',
            'video_coding/main/source/session_info_unittest.cc',
            'video_coding/main/source/timing_unittest.cc',
            'video_coding/main/source/video_coding_robustness_unittest.cc',
            'video_coding/main/source/video_receiver_unittest.cc',
            'video_coding/main/source/video_sender_unittest.cc',
            'video_coding/main/source/qm_select_unittest.cc',
            'video_coding/main/source/test/stream_generator.cc',
            'video_coding/main/source/test/stream_generator.h',
            'video_coding/utility/quality_scaler_unittest.cc',
            'video_processing/main/test/unit_test/brightness_detection_test.cc',
            'video_processing/main/test/unit_test/content_metrics_test.cc',
            'video_processing/main/test/unit_test/deflickering_test.cc',
            'video_processing/main/test/unit_test/video_processing_unittest.cc',
            'video_processing/main/test/unit_test/video_processing_unittest.h',
          ],
          'conditions': [
            ['OS_RUNTIME=="winrt"', {
              'dependencies': [
                'webrtc_opus_fec_test',
              ],
              'dependencies!': [
                'desktop_capture', # TODO(WinRT) remove when desktop_capture is ported
                '<(webrtc_root)/modules/modules.gyp:video_capture',
              ],
              'sources!': [ # TODO(WinRT) remove this section when desktop_capture is ported
                'desktop_capture/desktop_and_cursor_composer_unittest.cc',
                'desktop_capture/desktop_region_unittest.cc',
                'desktop_capture/differ_block_unittest.cc',
                'desktop_capture/differ_unittest.cc',
                'desktop_capture/mouse_cursor_monitor_unittest.cc',
                'desktop_capture/screen_capturer_helper_unittest.cc',
                'desktop_capture/screen_capturer_mac_unittest.cc',
                'desktop_capture/screen_capturer_mock_objects.h',
                'desktop_capture/screen_capturer_unittest.cc',
                'desktop_capture/window_capturer_unittest.cc',
                'desktop_capture/win/cursor_unittest.cc',
                'desktop_capture/win/cursor_unittest_resources.h',
                'desktop_capture/win/cursor_unittest_resources.rc',
              ],
      }],
            ['enable_bwe_test_logging==1', {
              'defines': [ 'BWE_TEST_LOGGING_COMPILE_TIME_ENABLE=1' ],
            }, {
              'defines': [ 'BWE_TEST_LOGGING_COMPILE_TIME_ENABLE=0' ],
              'sources!': [
                'remote_bitrate_estimator/test/bwe_test_logging.cc'
              ],
            }],
            # Run screen/window capturer tests only on platforms where they are
            # supported.
            ['desktop_capture_supported==0', {
              'sources!': [
                'desktop_capture/desktop_and_cursor_composer_unittest.cc',
                'desktop_capture/mouse_cursor_monitor_unittest.cc',
                'desktop_capture/screen_capturer_helper_unittest.cc',
                'desktop_capture/screen_capturer_mac_unittest.cc',
                'desktop_capture/screen_capturer_mock_objects.h',
                'desktop_capture/screen_capturer_unittest.cc',
                'desktop_capture/window_capturer_unittest.cc',
              ],
            }],
            ['prefer_fixed_point==1', {
              'defines': [ 'WEBRTC_AUDIOPROC_FIXED_PROFILE' ],
            }, {
              'defines': [ 'WEBRTC_AUDIOPROC_FLOAT_PROFILE' ],
            }],
            #Todo (Winrt), this fails building machine, disabled it for now.
            #this is could be race condition when using msbuild.exe commandline.
            #The header files generated by 'protoc.exe' may be generated in another process.
            # we might be able to enable it when we switch to ninja build
            ['enable_protobuf==1 and OS_RUNTIME!="winrt"', {
              'defines': [
                'WEBRTC_AUDIOPROC_DEBUG_DUMP',
              ],
              'dependencies': [
                'audioproc_protobuf_utils',
                'audioproc_unittest_proto',
              ],
              'sources': [
                'audio_processing/audio_processing_impl_unittest.cc',
                'audio_processing/test/audio_processing_unittest.cc',
                'audio_processing/test/test_utils.h',
              ],
            }],
            ['build_libvpx==1', {
              'dependencies': [
                '<(libvpx_dir)/libvpx.gyp:libvpx',
              ],
            }],
            ['OS=="android"', {
              'dependencies': [
                '<(DEPTH)/testing/android/native_test.gyp:native_test_native_code',
              ],
              # Need to disable error due to the line in
              # base/android/jni_android.h triggering it:
              # const BASE_EXPORT jobject GetApplicationContext()
              # error: type qualifiers ignored on function return type
              'cflags': [
                '-Wno-ignored-qualifiers',
              ],
              'sources': [
                'audio_device/android/audio_device_unittest.cc',
                'audio_device/android/audio_manager_unittest.cc',
                'audio_device/android/ensure_initialized.cc',
                'audio_device/android/ensure_initialized.h',
              ],
            }],
            ['OS=="ios"', {
              'sources': [
                'video_coding/codecs/h264/h264_video_toolbox_nalu_unittest.cc',
                'audio_device/ios/audio_device_unittest_ios.cc',
              ],
              'mac_bundle_resources': [
                '<(DEPTH)/resources/audio_coding/speech_mono_16kHz.pcm',
                '<(DEPTH)/resources/audio_coding/testfile32kHz.pcm',
                '<(DEPTH)/resources/audio_coding/teststereo32kHz.pcm',
                '<(DEPTH)/resources/audio_device/audio_short16.pcm',
                '<(DEPTH)/resources/audio_device/audio_short44.pcm',
                '<(DEPTH)/resources/audio_device/audio_short48.pcm',
                '<(DEPTH)/resources/audio_processing/agc/agc_no_circular_buffer.dat',
                '<(DEPTH)/resources/audio_processing/agc/agc_pitch_gain.dat',
                '<(DEPTH)/resources/audio_processing/agc/agc_pitch_lag.dat',
                '<(DEPTH)/resources/audio_processing/agc/agc_spectral_peak.dat',
                '<(DEPTH)/resources/audio_processing/agc/agc_voicing_prob.dat',
                '<(DEPTH)/resources/audio_processing/agc/agc_with_circular_buffer.dat',
                '<(DEPTH)/resources/short_mixed_mono_48.dat',
                '<(DEPTH)/resources/short_mixed_mono_48.pcm',
                '<(DEPTH)/resources/short_mixed_stereo_48.dat',
                '<(DEPTH)/resources/short_mixed_stereo_48.pcm',
              ],
            }],
          ],
          # Disable warnings to enable Win64 build, issue 1323.
          'msvs_disabled_warnings': [
            4267,  # size_t to int truncation.
            4456, 4457, 4458, 4459, # local members hides previously defined memebers or function members or class members
			4311, 4312, 4302,
          ],
        },
        {
          'target_name': 'modules_tests',
          'type': '<(gtest_target_type)',
          'dependencies': [
            '<(DEPTH)/testing/gtest.gyp:gtest',
            '<(webrtc_root)/common.gyp:webrtc_common',
            '<(webrtc_root)/common_video/common_video.gyp:common_video',
            '<(webrtc_root)/modules/video_coding/codecs/vp8/vp8.gyp:webrtc_vp8',
            '<(webrtc_root)/modules/video_coding/codecs/vp9/vp9.gyp:webrtc_vp9',
            '<(webrtc_root)/system_wrappers/system_wrappers.gyp:system_wrappers',
            '<(webrtc_root)/test/metrics.gyp:metrics',
            '<(webrtc_root)/test/test.gyp:test_support',
            '<(webrtc_root)/test/test.gyp:test_support_main',
            'audio_coding_module',
            'rtp_rtcp',
            'video_codecs_test_framework',
            'webrtc_utility',
            'webrtc_video_coding',
          ],
          'defines': [
            '<@(audio_coding_defines)',
          ],
          'sources': [
            'audio_coding/main/test/APITest.cc',
            'audio_coding/main/test/Channel.cc',
            'audio_coding/main/test/EncodeDecodeTest.cc',
            'audio_coding/main/test/PCMFile.cc',
            'audio_coding/main/test/PacketLossTest.cc',
            'audio_coding/main/test/RTPFile.cc',
            'audio_coding/main/test/SpatialAudio.cc',
            'audio_coding/main/test/TestAllCodecs.cc',
            'audio_coding/main/test/TestRedFec.cc',
            'audio_coding/main/test/TestStereo.cc',
            'audio_coding/main/test/TestVADDTX.cc',
            'audio_coding/main/test/Tester.cc',
            'audio_coding/main/test/TimedTrace.cc',
            'audio_coding/main/test/TwoWayCommunication.cc',
            'audio_coding/main/test/iSACTest.cc',
            'audio_coding/main/test/initial_delay_unittest.cc',
            'audio_coding/main/test/opus_test.cc',
            'audio_coding/main/test/target_delay_unittest.cc',
            'audio_coding/main/test/utility.cc',
            'rtp_rtcp/test/testFec/test_fec.cc',
            'video_coding/codecs/test/videoprocessor_integrationtest.cc',
            'video_coding/codecs/vp8/test/vp8_impl_unittest.cc',
          ],
          'conditions': [
            ['OS=="android"', {
              'dependencies': [
                '<(DEPTH)/testing/android/native_test.gyp:native_test_native_code',
              ],
            }],
          ],
        },
      ],
      'conditions': [
        ['OS=="android"', {
          'targets': [
            {
              'target_name': 'modules_unittests_apk_target',
              'type': 'none',
              'dependencies': [
                '<(apk_tests_path):modules_unittests_apk',
              ],
            },
            {
              'target_name': 'modules_tests_apk_target',
              'type': 'none',
              'dependencies': [
                '<(apk_tests_path):modules_tests_apk',
              ],
            },
          ],
        }],
        ['test_isolation_mode != "noop"', {
          'targets': [
            {
              'target_name': 'modules_tests_run',
              'type': 'none',
              'dependencies': [
                'modules_tests',
              ],
              'includes': [
                '../build/isolate.gypi',
              ],
              'sources': [
                'modules_tests.isolate',
              ],
            },
            {
              'target_name': 'modules_unittests_run',
              'type': 'none',
              'dependencies': [
                'modules_unittests',
              ],
              'includes': [
                '../build/isolate.gypi',
              ],
              'sources': [
                'modules_unittests.isolate',
              ],
            },
          ],
        }],
      ],
    }], # include_tests
  ], # conditions
}
