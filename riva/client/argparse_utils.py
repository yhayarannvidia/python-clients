# SPDX-FileCopyrightText: Copyright (c) 2022 NVIDIA CORPORATION & AFFILIATES. All rights reserved.
# SPDX-License-Identifier: MIT

import argparse


def add_asr_config_argparse_parameters(
    parser: argparse.ArgumentParser, max_alternatives: bool = False, profanity_filter: bool = False, word_time_offsets: bool = False
) -> argparse.ArgumentParser:
    if word_time_offsets:
        parser.add_argument(
            "--word-time-offsets", default=False, action='store_true', help="Option to output word timestamps."
        )
    if max_alternatives:
        parser.add_argument(
            "--max-alternatives",
            default=1,
            type=int,
            help="Maximum number of alternative transcripts to return (up to limit configured on server).",
        )
    if profanity_filter:
        parser.add_argument(
        "--profanity-filter",
        default=False,
        action='store_true',
        help="Flag that controls the profanity filtering in the generated transcripts",
    )
    parser.add_argument(
        "--automatic-punctuation",
        default=False,
        action='store_true',
        help="Flag that controls if transcript should be automatically punctuated",
    )
    parser.add_argument(
        "--no-verbatim-transcripts",
        default=False,
        action='store_true',
        help="If specified, text inverse normalization will be applied",
    )
    parser.add_argument("--language-code", default="en-US", help="Language code of the model to be used.")
    parser.add_argument("--model-name", default="", help="Model name to be used.")
    parser.add_argument("--boosted-lm-words", action='append', help="Words to boost when decoding. Can be used multiple times to boost multiple words.")
    parser.add_argument(
        "--boosted-lm-score", type=float, default=4.0, help="Recommended range for the boost score is 20 to 100. The higher the boost score, the more biased the ASR engine is towards this word."
    )
    parser.add_argument(
        "--speaker-diarization",
        default=False,
        action='store_true',
        help="Flag that controls if speaker diarization should be performed",
    )
    parser.add_argument(
        "--diarization-max-speakers",
        default=3,
        type=int,
        help="Max number of speakers to detect when performing speaker diarization",
    )
    parser.add_argument(
        "--start-history",
        default=-1,
        type=int,
        help="Value (in milliseconds) to detect and initiate start of speech utterance",
    )
    parser.add_argument(
        "--start-threshold",
        default=-1.0,
        type=float,
        help="Threshold value for detecting the start of speech utterance",
    )
    parser.add_argument(
        "--stop-history",
        default=-1,
        type=int,
        help="Value (in milliseconds) to detect end of utterance and reset decoder",
    )
    parser.add_argument(
        "--stop-threshold",
        default=-1.0,
        type=float,
        help="Threshold value for detecting the end of speech utterance",
    )
    parser.add_argument(
        "--stop-history-eou",
        default=-1,
        type=int,
        help="Value (in milliseconds) to detect end of utterance for the 1st pass and generate an intermediate final transcript",
    )
    parser.add_argument(
        "--stop-threshold-eou",
        default=-1.0,
        type=float,
        help="Threshold value for likelihood of blanks before detecting end of utterance",
    )
    parser.add_argument(
        "--custom-configuration",
        default="",
        type=str,
        help="Custom configurations to be sent to the server as key value pairs <key:value,key:value,...>",
    )
    return parser


def add_connection_argparse_parameters(parser: argparse.ArgumentParser) -> argparse.ArgumentParser:
    parser.add_argument("--server", default="localhost:50051", help="URI to GRPC server endpoint.")
    parser.add_argument("--ssl-cert", help="Path to SSL client certificates file.")
    parser.add_argument(
        "--use-ssl", action='store_true', help="Boolean to control if SSL/TLS encryption should be used."
    )
    parser.add_argument("--metadata", action='append', nargs='+', help="Send HTTP Header(s) to server")
    parser.add_argument(
        "--max-message-length", type=int, default=64 * 1024 * 1024, help="Maximum message length for GRPC server."
    )
    return parser

def add_realtime_config_argparse_parameters(parser: argparse.ArgumentParser) -> argparse.ArgumentParser:
    parser.add_argument("--endpoint", default="/v1/realtime", help="Endpoint to WebSocket server endpoint.")
    parser.add_argument("--query-params", default="intent=transcription", help="Query parameters to WebSocket server endpoint.")
    return parser