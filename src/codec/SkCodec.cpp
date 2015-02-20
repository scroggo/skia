/*
 * Copyright 2015 Google Inc.
 *
 * Use of this source code is governed by a BSD-style license that can be
 * found in the LICENSE file.
 */

#include "SkCodec.h"
#include "SkData.h"
#include "SkCodec_libpng.h"
#include "SkStream.h"

SkCodec* SkCodec::NewFromStream(SkStream* stream) {
    if (!stream) {
        return NULL;
    }
    SkAutoTDelete<SkStream> streamDeleter(stream);
    const bool isPng = SkPngCodec::IsPng(stream);
    if (!stream->rewind()) {
        return NULL;
    }
    if (isPng) {
        streamDeleter.detach();
        return SkPngCodec::NewFromStream(stream);
    }
    // TODO: Check other image types.
    return NULL;
}

SkCodec* SkCodec::NewFromData(SkData* data) {
    if (!data) {
        return NULL;
    }
    return NewFromStream(SkNEW_ARGS(SkMemoryStream, (data)));
}

SkCodec::SkCodec(const SkImageInfo& info, SkStream* stream)
    : fInfo(info)
    , fStream(stream)
{}