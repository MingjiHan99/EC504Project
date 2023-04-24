
#include <iostream>
#include <memory>
#include <random>

#include <chrono>
#include <optional>
using namespace std;
using namespace std::chrono;

template<typename K, typename V>
struct Node {
    K key;
    V value;
    vector<shared_ptr<Node> > next_ptrs;
    int level;
    Node(const K& key, const V& value, const int& level) : key(key), value(value), level(level), next_ptrs(level, nullptr) {
    }
};

template<typename K, typename V>
class SkipList {
public:
    SkipList(const double& p, const int& max_level) : p(p), max_level(max_level),distribution(0.0, 1.0) {
        head = make_shared<Node<K, V> >(K(), V(), max_level);
    }

    void set(const K& key, const V& value) {
        int level = random_level();
        shared_ptr<Node<K, V> > node = make_shared<Node<K, V> >(key, value, level);
        auto p = head;
        for (int i = max_level - 1; i >= 0; --i) {
            while (p->next_ptrs[i] != nullptr && p->next_ptrs[i]->key < key) {
                p = p->next_ptrs[i];
            }
            if (i < level) {
                node->next_ptrs[i] = p->next_ptrs[i];
                p->next_ptrs[i] = node;
            }
        }
    }
    
    void remove(const K& key) {
       
        vector<shared_ptr<Node<K, V> > > prev_ptrs(max_level, nullptr);
        auto p = head;
        for (int i = max_level - 1; i >= 0; --i) {
            while (p->next_ptrs[i] != nullptr && p->next_ptrs[i]->key < key) {
                p = p->next_ptrs[i];
            }
            prev_ptrs[i] = p;
        }
        for (int i = 0; i < max_level; ++i) {
            if (prev_ptrs[i]->next_ptrs[i]->key != key) {
                break;
            }
            prev_ptrs[i]->next_ptrs[i] = prev_ptrs[i]->next_ptrs[i]->next_ptrs[i];
        }
    }

    optional<V> get(const V& key) {
        auto ptr = find_ptr(key);
        if (ptr != nullptr) {
            return ptr->value;
        }
        return {};
    }

    int random_level() {
        int level = 1;
        while (distribution(generator) < p && level < max_level) {
            ++level;
        }
        return level;
    }
    friend std::ostream& operator<< (std::ostream& os, const SkipList<K, V>& skip_list) {
        for (int i = skip_list.max_level - 1; i >= 0; --i) {
            auto p = skip_list.head->next_ptrs[i];
            while (p != nullptr) {
                os << p->key << " ";
                p = p->next_ptrs[i];
            }
            os << endl;
        }
        return os;
    }    

private:
    shared_ptr<Node<K, V>> find_ptr(const K& key) {
        auto p = head;
        for (int i = max_level - 1; i >= 0; --i) {
            while (p->next_ptrs[i] != nullptr && p->next_ptrs[i]->key < key) {
                p = p->next_ptrs[i];
            }
            if (p->next_ptrs[i] != nullptr && p->next_ptrs[i]->key == key) {
                return p->next_ptrs[i];
            }
        }
        return nullptr;
    }
    default_random_engine generator;
    uniform_real_distribution<double> distribution;
    shared_ptr<Node<K, V>> head;
    int max_level;
    double p;
};

int main() {
    
    vector<int> sizes = {10000, 50000, 100000, 500000, 1000000};
    vector<double> times = {0.0, 0.0, 0.0, 0.0, 0.0};
    for (int i = 0; i < 5; ++i) {
        SkipList<int, int> skiplist(0.5, 32);
        auto insertion_start = high_resolution_clock::now();
        for (int j = 0; j < sizes[i]; ++j) {
            skiplist.set(j, j);
        }
        auto insertion_end = high_resolution_clock::now();
        std::chrono::duration<double, milli> fp_ms_insertion = insertion_end - insertion_start;
        times[i] = fp_ms_insertion.count();

        cout << "Querying: " << endl;
        auto query_start = high_resolution_clock::now();
       
        for (int j = 0; j < sizes[i] ; ++j) {
            skiplist.get(j);
        }
        auto query_end = high_resolution_clock::now();
        std::chrono::duration<double, milli> fp_ms_deletion = query_end - query_start;
        times[i] = fp_ms_deletion.count();
        cout << times[i] << endl;
    }

    for (int i = 0 ;i < 5; ++i) {
        cout << sizes[i] << " " << times[i] / 1000.0 << endl;
    }
    return 0;
}