#pragma once
#define _ATL_APARTMENT_THREADED

#include <atlbase.h>
//You may derive a class from CComModule and use it if you want to override something,
//but do not change the name of _Module
extern CComModule _Module;
#include <atlcom.h>
#pragma comment(lib,"sapi.lib") //导入语音头文件库
#include <sphelper.h>//语音识别头文件
#include <atlstr.h>//要用到CString

const int WM_RECORD = WM_USER + 100;//定义消息
CComPtr<ISpRecognizer>m_cpRecoEngine;// 语音识别引擎(recognition)的接口。
CComPtr<ISpRecoContext>m_cpRecoCtxt;// 识别引擎上下文(context)的接口。
CComPtr<ISpRecoGrammar>m_cpDictationGrammar;// 识别文法(grammar)的接口。
CComPtr<ISpStream>m_cpInputStream;// 流()的接口。
CComPtr<ISpObjectToken>m_cpToken;// 语音特征的(token)接口。
CComPtr<ISpAudio>m_cpAudio;// 音频(Audio)的接口。(用来保存原来默认的输入流)
ULONGLONG  GIDDICTATION;