#!/usr/bin/env swift
import Vision
import AppKit
import Foundation

guard CommandLine.arguments.count >= 2 else {
    print("用法: swift imgocr.swift <图片路径>")
    exit(1)
}

let path = CommandLine.arguments[1]
guard let img = NSImage(contentsOfFile: path),
      let cgImg = img.cgImage(forProposedRect: nil, context: nil, hints: nil) else {
    print("无法读取图片: \(path)")
    exit(1)
}

let req = VNRecognizeTextRequest()
req.recognitionLevel = .accurate
req.usesLanguageCorrection = true
// 支持中文
req.recognitionLanguages = ["zh-Hans", "zh-Hant", "en"]

let handler = VNImageRequestHandler(cgImage: cgImg, options: [:])
do {
    try handler.perform([req])
} catch {
    print("OCR 失败: \(error)")
    exit(1)
}

guard let results = req.results else {
    print("无识别结果")
    exit(0)
}

for obs in results {
    let text = obs.topCandidates(1).first?.string ?? ""
    guard !text.isEmpty else { continue }
    let bbox = obs.boundingBox
    // boundingBox 是归一化坐标 (左下角原点)
    let x = Int(bbox.origin.x * 100)
    let y = Int(bbox.origin.y * 100)
    let w = Int(bbox.size.width * 100)
    let printX = x
    let printY = 100 - y - w  // 转为左上角
    print("[\(printX),\(printY)] \(text)")
}
