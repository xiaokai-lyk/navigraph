#pragma once
#define _ATL_APARTMENT_THREADED

#include <atlbase.h>
//You may derive a class from CComModule and use it if you want to override something,
//but do not change the name of _Module
extern CComModule _Module;
#include <atlcom.h>
#pragma comment(lib,"sapi.lib") //��������ͷ�ļ���
#include <sphelper.h>//����ʶ��ͷ�ļ�
#include <atlstr.h>//Ҫ�õ�CString

const int WM_RECORD = WM_USER + 100;//������Ϣ
CComPtr<ISpRecognizer>m_cpRecoEngine;// ����ʶ������(recognition)�Ľӿڡ�
CComPtr<ISpRecoContext>m_cpRecoCtxt;// ʶ������������(context)�Ľӿڡ�
CComPtr<ISpRecoGrammar>m_cpDictationGrammar;// ʶ���ķ�(grammar)�Ľӿڡ�
CComPtr<ISpStream>m_cpInputStream;// ��()�Ľӿڡ�
CComPtr<ISpObjectToken>m_cpToken;// ����������(token)�ӿڡ�
CComPtr<ISpAudio>m_cpAudio;// ��Ƶ(Audio)�Ľӿڡ�(��������ԭ��Ĭ�ϵ�������)
ULONGLONG  GIDDICTATION;